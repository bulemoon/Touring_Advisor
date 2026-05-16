import os
import httpx
from fastapi import APIRouter

router = APIRouter()

AMAP_SERVER_KEY = os.getenv("AMAP_SERVER_KEY", "")


@router.get("/api/location/ip")
async def ip_location():
    """通过高德 REST API 做 IP 定位，避免前端跨域问题"""
    async with httpx.AsyncClient(timeout=8.0) as client:
        resp = await client.get(
            "https://restapi.amap.com/v3/ip",
            params={"key": AMAP_SERVER_KEY},
        )
        data = resp.json()

    if data.get("status") == "1" and data.get("rectangle"):
        parts = data["rectangle"].split(";")
        p1 = list(map(float, parts[0].split(",")))
        p2 = list(map(float, parts[1].split(",")))
        return {
            "success": True,
            "lat": (p1[1] + p2[1]) / 2,
            "lng": (p1[0] + p2[0]) / 2,
            "city": data.get("city", ""),
            "province": data.get("province", ""),
        }

    return {"success": False}
