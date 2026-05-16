from __future__ import annotations

import os
import time
from typing import Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.tour import TourRoute
from db.models.user import User
from db.session import get_db
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


class HighlightSourceResponse(BaseModel):
    title: str
    address: str
    distance_m: int
    cover_url: str
    intro: str
    zhihu_keyword: str
    zhihu_notes: list[dict]
    lat: float
    lng: float


def _amap_key() -> str:
    return os.getenv("AMAP_SERVER_KEY", "")


def _zhihu_secret() -> str:
    return os.getenv("ZHIHU_ACCESS_SECRET", "")


def _static_map_url(lat: float, lng: float, label: str) -> str:
    key = _amap_key()
    if not key:
        return ""
    return (
        "https://restapi.amap.com/v3/staticmap"
        f"?key={key}&location={lng},{lat}&zoom=15&size=640*360&scale=2"
        f"&markers=mid,0xD8BF79,A:{lng},{lat}&labels={label.replace(' ', '')},{lng},{lat},1,0xD8BF79,0x1F1813"
    )


async def _search_zhihu(query: str) -> list[dict]:
    secret = _zhihu_secret()
    if not secret:
        return []

    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            response = await client.get(
                "https://developer.zhihu.com/api/v1/content/zhihu_search",
                params={"Query": query, "Count": 3},
                headers={
                    "Authorization": f"Bearer {secret}",
                    "X-Request-Timestamp": str(int(time.time())),
                    "Content-Type": "application/json",
                },
            )
            data = response.json()
    except Exception:
        return []

    items = data.get("Items") or data.get("items") or []
    notes: list[dict] = []
    for item in items[:3]:
        notes.append(
            {
                "title": item.get("Title", ""),
                "summary": item.get("ContentText", "") or item.get("Summary", ""),
                "url": item.get("Url", ""),
                "author": item.get("AuthorName", ""),
            }
        )
    return notes


async def _search_amap_pois(lat: float, lng: float, radius: int = 5000) -> list[dict]:
    key = _amap_key()
    if not key:
        return []

    poi_types = ["旅游景点", "文化场馆", "风景名胜", "餐饮服务", "购物服务"]
    pois: list[dict] = []
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            for poi_type in poi_types:
                response = await client.get(
                    "https://restapi.amap.com/v3/place/around",
                    params={
                        "key": key,
                        "location": f"{lng},{lat}",
                        "radius": radius,
                        "types": poi_type,
                        "offset": 6,
                        "page": 1,
                        "extensions": "base",
                    },
                )
                data = response.json()
                if data.get("status") != "1":
                    continue
                for item in data.get("pois", []):
                    location = item.get("location", "")
                    poi_lng, poi_lat = (location.split(",") + ["0", "0"])[:2]
                    pois.append(
                        {
                            "name": item.get("name", ""),
                            "address": item.get("address", ""),
                            "type": item.get("type", ""),
                            "distance_m": int(float(item.get("distance", 0) or 0)),
                            "lat": float(poi_lat or 0),
                            "lng": float(poi_lng or 0),
                        }
                    )
    except Exception:
        return []

    seen = set()
    unique: list[dict] = []
    for poi in pois:
        key_name = poi["name"]
        if key_name and key_name not in seen:
            seen.add(key_name)
            unique.append(poi)
    return unique


def _route_keywords(tour: TourRoute) -> list[str]:
    text = f"{tour.title} {tour.description} {tour.city}"
    keywords = []
    for token in ["鼓浪屿", "厦门", "博物馆", "海边", "咖啡", "老街", "花园", "古厝", "文艺", "海景"]:
        if token in text:
            keywords.append(token)
    if not keywords:
        keywords = [tour.city or tour.title]
    return keywords[:3]


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
        query = query.order_by(func.abs(TourRoute.lat - lat) + func.abs(TourRoute.lng - lng))
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


@router.get("/{tour_id}/highlights")
async def get_tour_highlights(
    tour_id: int,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(TourRoute).where(TourRoute.id == tour_id))
    tour = result.scalar_one_or_none()
    if tour is None:
        raise HTTPException(status_code=404, detail="Tour not found")

    base_lat = lat if lat is not None else tour.lat
    base_lng = lng if lng is not None else tour.lng
    pois = await _search_amap_pois(base_lat, base_lng)
    keywords = _route_keywords(tour)

    highlights: list[dict] = []
    for poi in pois[:4]:
        keyword = keywords[len(highlights) % len(keywords)]
        zhihu_query = f"{tour.title} {keyword}" if keyword else tour.title
        zhihu_notes = await _search_zhihu(zhihu_query)
        highlights.append(
            HighlightSourceResponse(
                title=poi["name"],
                address=poi["address"] or tour.city,
                distance_m=poi["distance_m"],
                cover_url=_static_map_url(poi["lat"], poi["lng"], poi["name"]),
                intro=f"结合 {tour.title} 的节奏，适合安排到这一站。",
                zhihu_keyword=zhihu_query,
                zhihu_notes=zhihu_notes,
                lat=poi["lat"],
                lng=poi["lng"],
            ).model_dump()
        )

    if not highlights:
        highlights = await _mock_lingang_highlights()

    return {
        "tour": TourRouteResponse.model_validate(tour),
        "highlights": highlights,
    }


async def _mock_lingang_highlights() -> list[dict]:
    mocks = [
        {
            "title": "滴水湖",
            "address": "上海市浦东新区南汇新城镇环湖西一路",
            "distance_m": 1200,
            "intro": "适合作为临港路线的开场点，湖景开阔，日落和骑行体验都稳定。",
            "zhihu_keyword": "上海临港 滴水湖",
            "lat": 30.9023,
            "lng": 121.9298,
            "notes": [
                {
                    "title": "滴水湖值得怎么逛",
                    "summary": "看日落、骑行、湖边散步是最稳的玩法。",
                    "url": "",
                    "author": "Mock",
                }
            ],
        },
        {
            "title": "中国航海博物馆",
            "address": "上海市浦东新区申港大道197号",
            "distance_m": 2600,
            "intro": "适合接在滴水湖之后，内容完整，室内参观也更稳，适合半日路线收束。",
            "zhihu_keyword": "上海临港 航海博物馆",
            "lat": 30.9075,
            "lng": 121.9186,
            "notes": [
                {
                    "title": "航海博物馆参观体验",
                    "summary": "适合拍建筑外观，也适合带着主题逛展。",
                    "url": "",
                    "author": "Mock",
                }
            ],
        },
    ]

    results: list[dict] = []
    for item in mocks:
        zhihu_notes = await _search_zhihu(item["zhihu_keyword"])
        results.append(
            HighlightSourceResponse(
                title=item["title"],
                address=item["address"],
                distance_m=item["distance_m"],
                cover_url=_static_map_url(item["lat"], item["lng"], item["title"]),
                intro=item["intro"],
                zhihu_keyword=item["zhihu_keyword"],
                zhihu_notes=zhihu_notes or item["notes"],
                lat=item["lat"],
                lng=item["lng"],
            ).model_dump()
        )
    return results


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
