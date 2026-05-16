import random
import string
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.models.cart import CartItem
from db.models.order import Order, OrderItem
from db.models.user import User
from .deps import get_current_user

router = APIRouter(prefix="/api", tags=["orders"])


def _gen_order_no() -> str:
    return "TA" + "".join(random.choices(string.digits, k=14))


class AddCartRequest(BaseModel):
    product_name: str
    product_image: str = ""
    product_url: str = ""
    price: float = 0
    quantity: int = 1
    shop_name: str = ""


class CartItemResponse(BaseModel):
    id: int
    product_name: str
    product_image: str
    price: float
    quantity: int
    shop_name: str


class QuickOrderRequest(BaseModel):
    product_name: str
    product_image: str = ""
    product_url: str = ""
    price: float = 0
    quantity: int = 1
    shop_name: str = ""
    receiver_name: str = ""
    receiver_phone: str = ""
    receiver_address: str = ""


class OrderResponse(BaseModel):
    order_no: str
    total_amount: float
    status: str
    created_at: str


# --- Cart ---

@router.get("/cart")
async def list_cart(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(CartItem).where(CartItem.user_id == user.id)
    )
    items = result.scalars().all()
    return [CartItemResponse.model_validate(i) for i in items]


@router.post("/cart")
async def add_to_cart(
    req: AddCartRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    item = CartItem(
        user_id=user.id,
        product_name=req.product_name,
        product_image=req.product_image,
        product_url=req.product_url,
        price=req.price,
        quantity=req.quantity,
        shop_name=req.shop_name,
    )
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return CartItemResponse.model_validate(item)


@router.delete("/cart/{item_id}")
async def remove_cart_item(
    item_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(CartItem).where(CartItem.id == item_id, CartItem.user_id == user.id)
    )
    item = result.scalar_one_or_none()
    if item is None:
        raise HTTPException(status_code=404, detail="Cart item not found")
    await db.delete(item)
    await db.commit()
    return {"success": True}


# --- Orders ---

@router.post("/orders/quick")
async def quick_order(
    req: QuickOrderRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    total = req.price * req.quantity
    order = Order(
        order_no=_gen_order_no(),
        user_id=user.id,
        total_amount=total,
        receiver_name=req.receiver_name,
        receiver_phone=req.receiver_phone,
        receiver_address=req.receiver_address,
    )
    db.add(order)
    await db.flush()

    item = OrderItem(
        order_id=order.id,
        product_name=req.product_name,
        product_image=req.product_image,
        product_url=req.product_url,
        price=req.price,
        quantity=req.quantity,
        shop_name=req.shop_name,
    )
    db.add(item)
    await db.commit()
    await db.refresh(order)
    return {"success": True, "order_no": order.order_no, "total_amount": total}


@router.get("/orders")
async def list_orders(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Order).where(Order.user_id == user.id).order_by(Order.created_at.desc())
    )
    orders = result.scalars().all()
    return [OrderResponse.model_validate(o) for o in orders]


@router.get("/orders/{order_id}")
async def get_order(
    order_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Order).where(Order.id == order_id, Order.user_id == user.id)
    )
    order = result.scalar_one_or_none()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderResponse.model_validate(order)
