from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Literal

import httpx

CoordSystem = Literal["auto", "wgs84", "gcj02"]
TravelMode = Literal["walking", "driving"]


@dataclass
class RawStop:
    name: str
    lat: float
    lng: float
    address: str = ""
    city: str = ""
    duration_minutes: int = 60


@dataclass
class PlannedStop:
    name: str
    address: str
    lat: float
    lng: float
    original_lat: float
    original_lng: float
    duration_minutes: int
    sort_order: int
    coord_source: str
    correction_distance_m: int


_X_PI = math.pi * 3000.0 / 180.0
_PI = math.pi
_A = 6378245.0
_EE = 0.00669342162296594323


def amap_key() -> str:
    return os.getenv("AMAP_SERVER_KEY", "")


def out_of_china(lat: float, lng: float) -> bool:
    return lng < 72.004 or lng > 137.8347 or lat < 0.8293 or lat > 55.8271


def _transform_lat(lng: float, lat: float) -> float:
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + 0.1 * lng * lat + 0.2 * math.sqrt(abs(lng))
    ret += (20.0 * math.sin(6.0 * lng * _PI) + 20.0 * math.sin(2.0 * lng * _PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * _PI) + 40.0 * math.sin(lat / 3.0 * _PI)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * _PI) + 320 * math.sin(lat * _PI / 30.0)) * 2.0 / 3.0
    return ret


def _transform_lng(lng: float, lat: float) -> float:
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + 0.1 * lng * lat + 0.1 * math.sqrt(abs(lng))
    ret += (20.0 * math.sin(6.0 * lng * _PI) + 20.0 * math.sin(2.0 * lng * _PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * _PI) + 40.0 * math.sin(lng / 3.0 * _PI)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * _PI) + 300.0 * math.sin(lng / 30.0 * _PI)) * 2.0 / 3.0
    return ret


def wgs84_to_gcj02(lat: float, lng: float) -> tuple[float, float]:
    if out_of_china(lat, lng):
        return lat, lng
    dlat = _transform_lat(lng - 105.0, lat - 35.0)
    dlng = _transform_lng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * _PI
    magic = math.sin(radlat)
    magic = 1 - _EE * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((_A * (1 - _EE)) / (magic * sqrtmagic) * _PI)
    dlng = (dlng * 180.0) / (_A / sqrtmagic * math.cos(radlat) * _PI)
    return lat + dlat, lng + dlng


def haversine_m(a_lat: float, a_lng: float, b_lat: float, b_lng: float) -> int:
    radius = 6371000
    phi1 = math.radians(a_lat)
    phi2 = math.radians(b_lat)
    dphi = math.radians(b_lat - a_lat)
    dlambda = math.radians(b_lng - a_lng)
    h = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return int(2 * radius * math.asin(math.sqrt(h)))


async def _amap_text_search(client: httpx.AsyncClient, stop: RawStop, key: str) -> dict | None:
    if not key or not stop.name:
        return None
    try:
        response = await client.get(
            "https://restapi.amap.com/v3/place/text",
            params={
                "key": key,
                "keywords": stop.name,
                "city": stop.city,
                "citylimit": "true" if stop.city else "false",
                "offset": 5,
                "page": 1,
                "extensions": "base",
            },
        )
        data = response.json()
    except Exception:
        return None
    if data.get("status") != "1":
        return None

    candidates = []
    for poi in data.get("pois", []):
        location = poi.get("location", "")
        try:
            lng, lat = [float(v) for v in location.split(",")[:2]]
        except (TypeError, ValueError):
            continue
        candidates.append(
            {
                "name": poi.get("name") or stop.name,
                "address": poi.get("address") or stop.address,
                "lat": lat,
                "lng": lng,
                "distance": haversine_m(stop.lat, stop.lng, lat, lng),
            }
        )
    if not candidates:
        return None
    return min(candidates, key=lambda item: item["distance"])


async def normalize_stop(client: httpx.AsyncClient, stop: RawStop, coord_system: CoordSystem, key: str) -> PlannedStop:
    poi = await _amap_text_search(client, stop, key)
    if poi and poi["distance"] <= 5000:
        return PlannedStop(
            name=poi["name"],
            address=poi["address"],
            lat=poi["lat"],
            lng=poi["lng"],
            original_lat=stop.lat,
            original_lng=stop.lng,
            duration_minutes=stop.duration_minutes,
            sort_order=0,
            coord_source="amap_poi",
            correction_distance_m=poi["distance"],
        )

    lat, lng = stop.lat, stop.lng
    source = "input_gcj02"
    if coord_system in ("auto", "wgs84") and not out_of_china(lat, lng):
        lat, lng = wgs84_to_gcj02(lat, lng)
        source = "wgs84_to_gcj02"

    return PlannedStop(
        name=stop.name,
        address=stop.address,
        lat=lat,
        lng=lng,
        original_lat=stop.lat,
        original_lng=stop.lng,
        duration_minutes=stop.duration_minutes,
        sort_order=0,
        coord_source=source,
        correction_distance_m=haversine_m(stop.lat, stop.lng, lat, lng),
    )


def nearest_neighbor_order(stops: list[PlannedStop], start: PlannedStop | None = None) -> list[PlannedStop]:
    if len(stops) <= 2:
        return stops
    remaining = stops[:]
    ordered: list[PlannedStop] = []
    current = start or remaining.pop(0)
    if start is None:
        ordered.append(current)

    while remaining:
        next_stop = min(remaining, key=lambda item: haversine_m(current.lat, current.lng, item.lat, item.lng))
        remaining.remove(next_stop)
        ordered.append(next_stop)
        current = next_stop
    return ordered


def split_days(stops: list[PlannedStop], days: int) -> list[list[PlannedStop]]:
    days = max(1, min(days, max(1, len(stops))))
    groups = [[] for _ in range(days)]
    for index, stop in enumerate(stops):
        groups[index * days // len(stops)].append(stop)
    return groups


async def _amap_segment(
    client: httpx.AsyncClient,
    origin: PlannedStop,
    destination: PlannedStop,
    mode: TravelMode,
    key: str,
) -> dict:
    straight_distance = haversine_m(origin.lat, origin.lng, destination.lat, destination.lng)
    fallback = {
        "from": origin.name,
        "to": destination.name,
        "distance_m": straight_distance,
        "duration_sec": max(60, int(straight_distance / 1.2)),
        "polyline": [[origin.lat, origin.lng], [destination.lat, destination.lng]],
        "source": "straight_line",
    }
    if not key:
        return fallback

    endpoint = "driving" if mode == "driving" else "walking"
    try:
        response = await client.get(
            f"https://restapi.amap.com/v3/direction/{endpoint}",
            params={
                "key": key,
                "origin": f"{origin.lng},{origin.lat}",
                "destination": f"{destination.lng},{destination.lat}",
                "extensions": "base",
            },
        )
        data = response.json()
    except Exception:
        return fallback
    if data.get("status") != "1":
        return fallback

    route = data.get("route") or {}
    paths = route.get("paths") or []
    if not paths:
        return fallback
    path = paths[0]
    points: list[list[float]] = []
    for step in path.get("steps", []):
        for pair in (step.get("polyline") or "").split(";"):
            try:
                lng, lat = [float(v) for v in pair.split(",")[:2]]
            except (TypeError, ValueError):
                continue
            if not points or points[-1] != [lat, lng]:
                points.append([lat, lng])

    return {
        "from": origin.name,
        "to": destination.name,
        "distance_m": int(float(path.get("distance") or straight_distance)),
        "duration_sec": int(float(path.get("duration") or fallback["duration_sec"])),
        "polyline": points or fallback["polyline"],
        "source": "amap_direction",
    }


async def build_route_plan(
    stops: list[RawStop],
    *,
    start: RawStop | None = None,
    days: int = 1,
    mode: TravelMode = "walking",
    coord_system: CoordSystem = "wgs84",
    optimize: bool = True,
) -> dict:
    key = amap_key()
    async with httpx.AsyncClient(timeout=8.0) as client:
        planned_stops = [await normalize_stop(client, stop, coord_system, key) for stop in stops]
        planned_start = await normalize_stop(client, start, coord_system, key) if start else None

        if optimize:
            planned_stops = nearest_neighbor_order(planned_stops, planned_start)

        for index, stop in enumerate(planned_stops, start=1):
            stop.sort_order = index

        day_groups = split_days(planned_stops, days)
        response_days = []
        total_distance = 0
        total_duration = 0
        full_polyline: list[list[float]] = []

        for day_index, group in enumerate(day_groups, start=1):
            segments = []
            day_distance = 0
            day_duration = 0
            previous = planned_start if day_index == 1 and planned_start else None
            points_to_route = ([previous] if previous else []) + group
            for origin, destination in zip(points_to_route, points_to_route[1:]):
                segment = await _amap_segment(client, origin, destination, mode, key)
                segments.append(segment)
                day_distance += segment["distance_m"]
                day_duration += segment["duration_sec"]
                for point in segment["polyline"]:
                    if not full_polyline or full_polyline[-1] != point:
                        full_polyline.append(point)

            total_distance += day_distance
            total_duration += day_duration
            response_days.append(
                {
                    "day": day_index,
                    "stops": [stop.__dict__ for stop in group],
                    "segments": segments,
                    "distance_m": day_distance,
                    "travel_duration_sec": day_duration,
                    "stay_duration_min": sum(stop.duration_minutes for stop in group),
                }
            )

        return {
            "coord_system": "gcj02",
            "mode": mode,
            "optimized": optimize,
            "start": planned_start.__dict__ if planned_start else None,
            "days": response_days,
            "stops": [stop.__dict__ for stop in planned_stops],
            "polyline": full_polyline or [[stop.lat, stop.lng] for stop in planned_stops],
            "distance_m": total_distance,
            "travel_duration_sec": total_duration,
        }
