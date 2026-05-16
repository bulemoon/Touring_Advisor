from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/products", tags=["products"])


class ProductResponse(BaseModel):
    id: int
    name: str
    image: str
    price: float
    shop_name: str
    product_url: str
    reason: str = ""


_MOCK_PRODUCTS = [
    {"id": 1, "name": "稻香村点心礼盒", "image": "", "price": 88.0, "shop_name": "稻香村旗舰店", "product_url": "", "reason": "北京特产经典伴手礼"},
    {"id": 2, "name": "故宫文创书签", "image": "", "price": 39.0, "shop_name": "故宫文创旗舰店", "product_url": "", "reason": "文化纪念品"},
    {"id": 3, "name": "景泰蓝手镯", "image": "", "price": 128.0, "shop_name": "非遗手工艺店", "product_url": "", "reason": "传统工艺精美饰品"},
]


@router.get("")
async def search_products(lat: Optional[float] = None, lng: Optional[float] = None):
    return [ProductResponse(**p) for p in _MOCK_PRODUCTS]


@router.post("/ai-recommend")
async def ai_recommend_products():
    return [ProductResponse(**p) for p in _MOCK_PRODUCTS]
