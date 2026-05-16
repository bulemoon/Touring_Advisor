import random
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.models.user import User
from .deps import create_access_token, get_current_user

router = APIRouter(prefix="/api/auth", tags=["auth"])

# MVP: in-memory verification codes
_verification_codes: dict[str, str] = {}


class SendCodeRequest(BaseModel):
    phone: str


class LoginRequest(BaseModel):
    phone: str
    code: str


class LoginResponse(BaseModel):
    token: str
    user_id: int


@router.post("/send-code")
async def send_code(req: SendCodeRequest):
    code = str(random.randint(100000, 999999))
    _verification_codes[req.phone] = code
    # TODO: integrate SMS provider
    print(f"[MVP] Verification code for {req.phone}: {code}")
    return {"success": True, "message": "Code sent (check server logs in MVP mode)"}


@router.post("/login")
async def login(req: LoginRequest, db: AsyncSession = Depends(get_db)):
    stored = _verification_codes.get(req.phone)
    if not stored or stored != req.code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid code")
    del _verification_codes[req.phone]

    result = await db.execute(select(User).where(User.phone == req.phone))
    user = result.scalar_one_or_none()
    if user is None:
        user = User(phone=req.phone)
        db.add(user)
        await db.commit()
        await db.refresh(user)

    token = create_access_token(user.id)
    return LoginResponse(token=token, user_id=user.id)


class UserProfile(BaseModel):
    id: int
    phone: str
    nickname: str
    avatar_url: str


@router.get("/user/profile")
async def get_profile(user: User = Depends(get_current_user)):
    return UserProfile(
        id=user.id,
        phone=user.phone,
        nickname=user.nickname,
        avatar_url=user.avatar_url,
    )
