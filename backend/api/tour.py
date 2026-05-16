from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from db.models.tour import TourRoute, Itinerary, ItineraryStop
from db.models.user import User
from .deps import get_current_user

router = APIRouter(prefix="/api/tours", tags=["tours"])


class TourRouteResponse(BaseModel):
    id: int
    title: str
    duration: str
    description: str
    cover_url: str
    city: str
    favorites_count: int
    lat: float
    lng: float


class ItineraryStopResponse(BaseModel):
    name: str
    address: str
    duration_minutes: int
    note: str
    sort_order: int


class TourDetailResponse(TourRouteResponse):
    stops: list[ItineraryStopResponse] = []


@router.get("")
async def list_tours(
    duration: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(TourRoute)
    if duration:
        query = query.where(TourRoute.duration == duration)
    if lat is not None and lng is not None:
        query = query.order_by(
            func.abs(TourRoute.lat - lat) + func.abs(TourRoute.lng - lng)
        )
    result = await db.execute(query)
    tours = result.scalars().all()
    return [TourRouteResponse.model_validate(t) for t in tours]


@router.get("/{tour_id}")
async def get_tour(tour_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TourRoute).where(TourRoute.id == tour_id))
    tour = result.scalar_one_or_none()
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    return TourRouteResponse.model_validate(tour)


@router.post("/{tour_id}/favorite")
async def favorite_tour(
    tour_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(TourRoute).where(TourRoute.id == tour_id))
    tour = result.scalar_one_or_none()
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")
    tour.favorites_count += 1
    await db.commit()
    return {"success": True, "favorites_count": tour.favorites_count}
