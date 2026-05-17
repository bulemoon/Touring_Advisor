from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from services.route_planner import RawStop, build_route_plan

router = APIRouter(prefix="/api/route-plan", tags=["route-plan"])


class RouteStopRequest(BaseModel):
    name: str
    lat: float
    lng: float
    address: str = ""
    city: str = ""
    duration_minutes: int = Field(default=60, ge=0)


class RoutePlanRequest(BaseModel):
    stops: list[RouteStopRequest]
    start: RouteStopRequest | None = None
    days: int = Field(default=1, ge=1, le=10)
    mode: Literal["walking", "driving"] = "walking"
    coord_system: Literal["auto", "wgs84", "gcj02"] = "wgs84"
    optimize: bool = True


@router.post("")
async def create_route_plan(request: RoutePlanRequest):
    if len(request.stops) < 2:
        raise HTTPException(status_code=400, detail="At least two stops are required")

    return await build_route_plan(
        [RawStop(**stop.model_dump()) for stop in request.stops],
        start=RawStop(**request.start.model_dump()) if request.start else None,
        days=request.days,
        mode=request.mode,
        coord_system=request.coord_system,
        optimize=request.optimize,
    )
