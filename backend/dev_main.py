"""
AI 旅伴助手 — 开发入口
多轮对话 → 收集行程信息 → 聚合 API → 生成推荐 + Session 持久化
"""
import os
import json
import uuid
import random
import re
import math
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Touring Advisor AI (Agent Mode)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== API Keys =====
AMAP_KEY = os.getenv("AMAP_SERVER_KEY", "")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "")
KIMI_KEY = os.getenv("KIMI_API_KEY", "")
ZHIHU_SECRET = os.getenv("ZHIHU_ACCESS_SECRET", "")
QWEATHER_KEY = os.getenv("QWEATHER_API_KEY", "")

# ===== Session 目录 =====
SESSION_DIR = Path(__file__).resolve().parent.parent / "session"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

# ===== Dialog 目录 =====
DIALOG_DIR = Path(__file__).resolve().parent.parent / "dialog"
DIALOG_DIR.mkdir(parents=True, exist_ok=True)




# ===== 内存缓存 =====
_AMAP_CACHE: dict[str, list[dict]] = {}
_ZHIHU_CACHE: dict[str, list[dict]] = {}
_WEATHER_CACHE: dict[str, dict] = {}
_sessions: dict[str, dict] = {}

# ===== 会话状态管理 =====
STEPS = ["destination", "date", "residence", "duration"]
STEP_PROMPTS = {
    "destination": "你想去哪个城市或具体景点？",
    "date": "你计划哪天出发？（例如：5月20日，或 下周六）",
    "residence": "你会住在哪里？（酒店名称或大概地址，方便我计算距离）",
    "duration": "行程时长是多久？（半日游 / 一日游 / 三日游）",
}

TOUR_DURATIONS = {
    "半日": "half-day",
    "半日游": "half-day",
    "一日": "1-day",
    "一日游": "1-day",
    "三日": "3-day",
    "三日游": "3-day",
    "多日": "3-day",
    "half-day": "half-day",
    "1-day": "1-day",
    "3-day": "3-day",
}


def _save_session(sid: str):
    """将会话持久化到文件夹：meta/chat/attractions/shopping 分文件保存"""
    sdir = SESSION_DIR / sid
    sdir.mkdir(parents=True, exist_ok=True)
    s = _sessions[sid]
    # meta.json — 会话元数据
    meta = {
        "id": s["id"],
        "state": s.get("state"),
        "step": s.get("step"),
        "inputs": s.get("inputs"),
        "created_at": s.get("created_at"),
        "destination_coords": (s.get("result") or {}).get("destination_coords"),
        "weather": (s.get("result") or {}).get("weather"),
        "gear": (s.get("result") or {}).get("gear"),
        "zhihu": (s.get("result") or {}).get("zhihu"),
        "summary": (s.get("result") or {}).get("summary"),
        "route_plan": (s.get("result") or {}).get("route_plan"),
    }
    with open(sdir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    # chat.json — 对话消息
    with open(sdir / "chat.json", "w", encoding="utf-8") as f:
        json.dump(s.get("messages", []), f, ensure_ascii=False, indent=2)
    # attractions.json
    result = s.get("result") or {}
    if result.get("attractions"):
        with open(sdir / "attractions.json", "w", encoding="utf-8") as f:
            json.dump(result["attractions"], f, ensure_ascii=False, indent=2)
    # shopping.json
    if result.get("shopping"):
        with open(sdir / "shopping.json", "w", encoding="utf-8") as f:
            json.dump(result["shopping"], f, ensure_ascii=False, indent=2)


def _load_sessions_from_disk():
    """从磁盘加载所有会话到内存（支持旧 .json 文件 + 新文件夹格式）"""
    # 1. 加载旧格式：{sid}.json
    for f in sorted(SESSION_DIR.glob("*.json"), reverse=True):
        sid = f.stem
        if sid in _sessions or sid == ".gitkeep":
            continue
        try:
            with open(f, "r", encoding="utf-8") as fp:
                _sessions[sid] = json.load(fp)
        except Exception:
            pass
    # 2. 加载新格式：{sid}/meta.json + chat.json + ...
    for sdir in sorted(SESSION_DIR.glob("*/"), reverse=True):
        sid = sdir.name
        if sid.startswith(".") or sid in _sessions:
            continue
        try:
            meta_file = sdir / "meta.json"
            if not meta_file.exists():
                continue
            with open(meta_file, "r", encoding="utf-8") as f:
                meta = json.load(f)
            chat_file = sdir / "chat.json"
            messages = []
            if chat_file.exists():
                with open(chat_file, "r", encoding="utf-8") as f:
                    messages = json.load(f)
            attr_file = sdir / "attractions.json"
            attractions = None
            if attr_file.exists():
                with open(attr_file, "r", encoding="utf-8") as f:
                    attractions = json.load(f)
            shop_file = sdir / "shopping.json"
            shopping = None
            if shop_file.exists():
                with open(shop_file, "r", encoding="utf-8") as f:
                    shopping = json.load(f)
            result = None
            if attractions or shopping or meta.get("summary"):
                result = {
                    "attractions": attractions or [],
                    "shopping": shopping or [],
                    "weather": meta.get("weather"),
                    "gear": meta.get("gear"),
                    "zhihu": meta.get("zhihu"),
                    "summary": meta.get("summary"),
                    "route_plan": meta.get("route_plan"),
                    "destination_coords": meta.get("destination_coords"),
                }
            _sessions[sid] = {
                "id": meta["id"],
                "state": meta.get("state"),
                "step": meta.get("step", 0),
                "inputs": meta.get("inputs", {}),
                "messages": messages,
                "result": result,
                "created_at": meta.get("created_at", ""),
            }
        except Exception as e:
            print(f"[Session] Load error for {sid}: {e}")


_load_sessions_from_disk()


# ===== Amap POI 搜索 =====
def search_nearby_pois(lat: float, lng: float, radius: int = 5000) -> list[dict]:
    cache_key = f"{lat:.4f},{lng:.4f},{radius}"
    if cache_key in _AMAP_CACHE:
        return _AMAP_CACHE[cache_key]
    all_pois = []
    types_list = ["060000", "050000", "070000", "110000"]
    for t in types_list:
        try:
            r = requests.get(
                "https://restapi.amap.com/v3/place/around",
                params={
                    "key": AMAP_KEY,
                    "location": f"{lng},{lat}",
                    "radius": radius,
                    "types": t,
                    "offset": 15,
                    "page": 1,
                    "extensions": "all",
                },
                timeout=5,
            )
            data = r.json()
            if data.get("status") == "1":
                for p in data.get("pois", []):
                    all_pois.append({
                        "name": p.get("name", ""),
                        "type": p.get("type", ""),
                        "address": p.get("address", ""),
                        "distance": p.get("distance", "0"),
                        "location": p.get("location", ""),
                        "rating": p.get("biz_ext", {}).get("rating", ""),
                    })
        except Exception as e:
            print(f"[Amap] POI error ({t}): {e}")
    seen = set()
    unique = []
    for p in all_pois:
        if p["name"] not in seen:
            seen.add(p["name"])
            unique.append(p)
    _AMAP_CACHE[cache_key] = unique
    return unique


def geocode_city(city: str) -> tuple[float, float] | None:
    """高德地理编码：城市名 → 坐标"""
    try:
        r = requests.get(
            "https://restapi.amap.com/v3/geocode/geo",
            params={"key": AMAP_KEY, "address": city, "city": city},
            timeout=5,
        )
        data = r.json()
        if data.get("status") == "1" and data.get("geocodes"):
            loc = data["geocodes"][0]["location"]
            lng, lat = loc.split(",")
            return float(lat), float(lng)
    except Exception as e:
        print(f"[Amap] Geocode error: {e}")
    return None


def haversine_m(a_lat: float, a_lng: float, b_lat: float, b_lng: float) -> int:
    radius = 6371000
    phi1 = math.radians(a_lat)
    phi2 = math.radians(b_lat)
    dphi = math.radians(b_lat - a_lat)
    dlambda = math.radians(b_lng - a_lng)
    h = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return int(2 * radius * math.asin(math.sqrt(h)))


def build_route_plan_from_text(full_reply: str, attractions: list[dict], duration: str) -> dict | None:
    valid = [
        item for item in attractions
        if isinstance(item.get("lat"), (int, float)) and isinstance(item.get("lng"), (int, float))
    ]
    if len(valid) < 2:
        return None

    day_count = 3 if duration == "3-day" else 1
    day_sections: list[tuple[int, str]] = []
    matches = list(re.finditer(r"(?:Day|D)\s*([1-9])|第([一二三四五六七八九])天", full_reply, flags=re.IGNORECASE))
    chinese_day = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9}
    for index, match in enumerate(matches):
        day = int(match.group(1)) if match.group(1) else chinese_day.get(match.group(2), index + 1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(full_reply)
        if day:
            day_sections.append((day, full_reply[start:end]))

    if not day_sections:
        day_sections = [(1, full_reply)]

    used_names: set[str] = set()
    days = []
    ordered_all = []

    for day, section in day_sections[:day_count]:
        stops = []
        for item in valid:
            name = item.get("name", "")
            if not name or name in used_names:
                continue
            if name in section:
                stops.append({
                    "name": name,
                    "address": item.get("address", ""),
                    "lat": item["lat"],
                    "lng": item["lng"],
                    "sort_order": len(ordered_all) + len(stops) + 1,
                    "duration_minutes": 60,
                    "tip": "来自本次攻略推荐",
                })
                used_names.add(name)
        days.append({"day": day, "stops": stops})
        ordered_all.extend(stops)

    if len(ordered_all) < 2:
        fallback_count = 9 if duration == "3-day" else 5
        ordered_all = []
        used_names = set()
        chunks = [[] for _ in range(day_count)]
        for index, item in enumerate(valid[:fallback_count]):
            stop = {
                "name": item.get("name", ""),
                "address": item.get("address", ""),
                "lat": item["lat"],
                "lng": item["lng"],
                "sort_order": index + 1,
                "duration_minutes": 60,
                "tip": "来自目的地周边推荐",
            }
            chunks[index * day_count // min(fallback_count, len(valid))].append(stop)
            ordered_all.append(stop)
            used_names.add(stop["name"])
        days = [{"day": index + 1, "stops": stops} for index, stops in enumerate(chunks)]

    response_days = []
    full_polyline = []
    total_distance = 0
    for day in days:
        stops = day["stops"]
        segments = []
        day_distance = 0
        polyline = [[stop["lat"], stop["lng"]] for stop in stops]
        for origin, destination in zip(stops, stops[1:]):
            distance = haversine_m(origin["lat"], origin["lng"], destination["lat"], destination["lng"])
            day_distance += distance
            segments.append({
                "from": origin["name"],
                "to": destination["name"],
                "distance_m": distance,
                "polyline": [[origin["lat"], origin["lng"]], [destination["lat"], destination["lng"]]],
                "source": "straight_line",
            })
        total_distance += day_distance
        for point in polyline:
            if not full_polyline or full_polyline[-1] != point:
                full_polyline.append(point)
        response_days.append({
            "day": day["day"],
            "stops": stops,
            "segments": segments,
            "polyline": polyline,
            "distance_m": day_distance,
        })

    return {
        "coord_system": "gcj02",
        "mode": "walking",
        "optimized": False,
        "days": response_days,
        "stops": ordered_all,
        "polyline": full_polyline,
        "distance_m": total_distance,
    }


# ===== 天气查询（Open-Meteo + QWeather 备用）=====
# Open-Meteo WMO Weather codes → 中文描述
WMO_CODES = {
    0: ("晴", 0), 1: ("晴间多云", 0), 2: ("多云", 0), 3: ("阴", 0),
    45: ("雾", 0.1), 48: ("雾凇", 0.1),
    51: ("小毛毛雨", 0.2), 53: ("毛毛雨", 0.5), 55: ("大毛毛雨", 1.0),
    61: ("小雨", 0.5), 63: ("中雨", 2.0), 65: ("大雨", 5.0),
    71: ("小雪", 0.5), 73: ("中雪", 2.0), 75: ("大雪", 5.0),
    77: ("雪粒", 0.3),
    80: ("阵雨", 1.0), 81: ("中阵雨", 3.0), 82: ("强阵雨", 5.0),
    85: ("小阵雪", 0.5), 86: ("大阵雪", 3.0),
    95: ("雷暴", 2.0), 96: ("雷暴+小冰雹", 3.0), 99: ("雷暴+大冰雹", 5.0),
}

def get_weather(city: str, date: str = "") -> dict | None:
    """查询目的地天气预报 (Open-Meteo 免费 API)"""
    try:
        coords = geocode_city(city)
        if not coords:
            # 尝试 QWeather 作为备用
            return _get_weather_qweather(city)
        lat, lng = coords[0], coords[1]

        r = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lng,
                "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max,uv_index_max",
                "timezone": "Asia/Shanghai",
                "forecast_days": 7,
            },
            timeout=10,
        )
        data = r.json()
        daily_data = data.get("daily", {})
        if not daily_data:
            return None

        days = []
        for i, d in enumerate(daily_data.get("time", [])):
            code = daily_data["weather_code"][i]
            text_day, precip_est = WMO_CODES.get(code, ("未知", 0))
            days.append({
                "date": d,
                "temp_max": str(daily_data["temperature_2m_max"][i]),
                "temp_min": str(daily_data["temperature_2m_min"][i]),
                "text_day": text_day,
                "text_night": text_day,
                "wind_dir": "",
                "wind_scale": str(daily_data.get("wind_speed_10m_max", [0])[i] or 0),
                "humidity": "",
                "uv_index": str(daily_data.get("uv_index_max", [0])[i] or 0),
                "precip": str(daily_data["precipitation_sum"][i]),
            })

        return {"city": city, "daily": days}
    except Exception as e:
        print(f"[Weather/OpenMeteo] Error: {e}")
    return _get_weather_qweather(city)


def _get_weather_qweather(city: str) -> dict | None:
    """QWeather 备用天气查询"""
    if not QWEATHER_KEY:
        return None
    try:
        geo_r = requests.get(
            "https://geoapi.qweather.com/v2/city/lookup",
            params={"key": QWEATHER_KEY, "location": city},
            timeout=5,
        )
        geo_data = geo_r.json()
        city_id = None
        if geo_data.get("code") == "200" and geo_data.get("location"):
            city_id = geo_data["location"][0]["id"]
        if not city_id:
            return None

        w_r = requests.get(
            "https://devapi.qweather.com/v7/weather/7d",
            params={"key": QWEATHER_KEY, "location": city_id},
            timeout=5,
        )
        w_data = w_r.json()
        if w_data.get("code") != "200":
            return None

        daily = w_data.get("daily", [])
        return {
            "city": city,
            "daily": [
                {
                    "date": d.get("fxDate", ""),
                    "temp_max": d.get("tempMax", ""),
                    "temp_min": d.get("tempMin", ""),
                    "text_day": d.get("textDay", ""),
                    "text_night": d.get("textNight", ""),
                    "wind_dir": d.get("windDirDay", ""),
                    "wind_scale": d.get("windScaleDay", ""),
                    "humidity": d.get("humidity", ""),
                    "uv_index": d.get("uvIndex", ""),
                    "precip": d.get("precip", ""),
                }
                for d in daily
            ],
        }
    except Exception as e:
        print(f"[QWeather] Error: {e}")
    return None


# ===== 知乎搜索 =====
def search_zhihu(query: str) -> list[dict]:
    if query in _ZHIHU_CACHE:
        return _ZHIHU_CACHE[query]
    results = []
    try:
        import time as _time
        r = requests.get(
            "https://developer.zhihu.com/api/v1/content/zhihu_search",
            params={"Query": query, "Count": 5},
            headers={
                "Authorization": f"Bearer {ZHIHU_SECRET}",
                "X-Request-Timestamp": str(int(_time.time())),
                "Content-Type": "application/json",
            },
            timeout=5,
        )
        data = r.json()
        for item in data.get("Items", []):
            results.append({
                "title": item.get("Title", ""),
                "snippet": item.get("ContentText", ""),
                "url": item.get("Url", ""),
            })
    except Exception as e:
        print(f"[Zhihu] Error: {e}")
    _ZHIHU_CACHE[query] = results
    return results


# ===== DeepSeek LLM =====
def call_deepseek(system: str, user: str) -> str:
    try:
        r = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {DEEPSEEK_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": 0.8,
                "max_tokens": 2500,
            },
            timeout=60,
        )
        data = r.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[DeepSeek] Error: {e}")
        return ""


# ===== 装备推荐 =====
def recommend_gear(weather: dict | None, terrain_tags: list[str] = None) -> list[dict]:
    """根据天气和地形推荐装备"""
    gear = []
    terrain_tags = terrain_tags or []

    if weather and weather.get("daily"):
        today = weather["daily"][0]
        temp_max = int(float(today.get("temp_max", 20) or 20))
        temp_min = int(float(today.get("temp_min", 10) or 10))
        uv = int(float(today.get("uv_index", 3) or 3))
        precip = float(today.get("precip", 0) or 0)
        text_day = today.get("text_day", "")
        wind_scale = int(float(today.get("wind_scale", 1) or 1))

        # 温度建议
        if temp_max > 30:
            gear.append({"name": "遮阳帽/太阳镜", "reason": f"最高温{temp_max}°C，注意防晒", "icon": "🧢"})
            gear.append({"name": "防晒霜", "reason": "高温天气必备", "icon": "🧴"})
        if temp_min < 10:
            gear.append({"name": "外套/薄羽绒", "reason": f"最低温{temp_min}°C，早晚较凉", "icon": "🧥"})
        if temp_min < 5:
            gear.append({"name": "保暖内衣/厚外套", "reason": f"低温{temp_min}°C，注意保暖", "icon": "🧣"})

        # 紫外线
        if uv >= 6:
            gear.append({"name": "高倍防晒霜 SPF50+", "reason": f"紫外线指数{uv}，强度很高", "icon": "☀️"})
            gear.append({"name": "遮阳伞/太阳镜", "reason": "强紫外线防护", "icon": "🕶️"})
        elif uv >= 3:
            gear.append({"name": "防晒霜", "reason": f"紫外线指数{uv}，建议防护", "icon": "☀️"})

        # 降雨
        if "雨" in text_day or precip > 0:
            gear.append({"name": "雨伞/雨衣", "reason": "预计有降雨，带好雨具", "icon": "🌂"})
            gear.append({"name": "防水鞋", "reason": "雨天路面湿滑", "icon": "👢"})

        # 风力
        if wind_scale >= 5:
            gear.append({"name": "防风外套", "reason": f"{wind_scale}级风，注意防风", "icon": "💨"})

    # 地形/场景建议
    for tag in terrain_tags:
        if tag in ("森林", "丛林", "山区", "爬山", "徒步"):
            gear.append({"name": "驱蚊水/驱蚊贴", "reason": "户外防虫必备", "icon": "🦟"})
            break
    for tag in terrain_tags:
        if tag in ("湖边", "海边", "沙滩", "水上", "漂流"):
            gear.append({"name": "凉鞋/拖鞋", "reason": "近水活动更方便", "icon": "🩴"})
            break

    return gear


# ===== Session 管理 =====
class SessionStartResponse(BaseModel):
    session_id: str
    message: str
    current_step: int
    current_step_name: str


class SessionListItem(BaseModel):
    session_id: str
    destination: str | None
    duration: str | None
    created_at: str
    message_count: int


class ChatRequest(BaseModel):
    message: str
    lat: float = 31.2304
    lng: float = 121.4737
    session_id: str | None = None


# ===== API 端点 =====

@app.get("/health")
async def health():
    return {"status": "ok", "mode": "agent"}


@app.post("/api/session/start")
async def start_session() -> SessionStartResponse:
    """创建新会话，开始引导式对话"""
    sid = uuid.uuid4().hex[:12]
    _sessions[sid] = {
        "id": sid,
        "state": "collecting",
        "step": 0,
        "inputs": {"destination": None, "date": None, "residence": None, "duration": None},
        "messages": [],
        "result": None,
        "created_at": datetime.utcnow().isoformat(),
    }
    key = STEPS[0]
    prompt = STEP_PROMPTS[key]
    _sessions[sid]["messages"].append({"role": "assistant", "content": prompt})
    _sessions[sid]["messages"].append({
        "role": "assistant",
        "content": "你好！我是你的 AI 旅伴助手。我会帮你规划一次完美的旅行。\n\n" + prompt,
    })
    _save_session(sid)
    return SessionStartResponse(
        session_id=sid,
        message=f"你好！我是你的 AI 旅伴助手。\n\n{prompt}",
        current_step=0,
        current_step_name=STEPS[0],
    )


@app.get("/api/session/list")
async def list_sessions() -> list[SessionListItem]:
    """列出所有历史会话"""
    items = []
    for sid, s in sorted(_sessions.items(), key=lambda x: x[1].get("created_at", ""), reverse=True):
        inp = s.get("inputs", {})
        items.append(SessionListItem(
            session_id=sid,
            destination=inp.get("destination"),
            duration=inp.get("duration"),
            created_at=s.get("created_at", ""),
            message_count=len(s.get("messages", [])),
        ))
    return items


@app.get("/api/session/{session_id}")
async def get_session(session_id: str):
    """获取指定会话详情"""
    if session_id not in _sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    return _sessions[session_id]


@app.delete("/api/session/all")
async def clear_all_sessions():
    """清空所有会话及对话记录"""
    _sessions.clear()
    errors = []
    deleted = []
    # 删除 session 目录所有文件和文件夹
    for item in list(SESSION_DIR.iterdir()):
        if item.name.startswith("."):
            continue
        try:
            if item.is_file():
                item.unlink()
                deleted.append(f"file:{item.name}")
            elif item.is_dir():
                import shutil
                shutil.rmtree(item)
                deleted.append(f"dir:{item.name}")
        except Exception as e:
            errors.append(f"{item.name}: {e}")
    # 删除 dialog 目录所有运行时历史记录（保留模板）
    for item in list(DIALOG_DIR.iterdir()):
        if item.name.startswith(".") or item.name in ("prompt.md", "output.md"):
            continue
        try:
            if item.is_file():
                item.unlink()
                deleted.append(f"dialog-file:{item.name}")
            elif item.is_dir():
                import shutil
                shutil.rmtree(item)
                deleted.append(f"dialog-dir:{item.name}")
        except Exception as e:
            errors.append(f"dialog-{item.name}: {e}")
    print(f"[ClearAll] deleted={deleted}, errors={errors}")
    return {"success": True, "deleted": len(deleted), "errors": errors}


@app.delete("/api/session/{session_id}")
async def delete_session(session_id: str):
    """删除指定会话"""
    if session_id in _sessions:
        del _sessions[session_id]
    # 删除文件/文件夹
    json_file = SESSION_DIR / f"{session_id}.json"
    folder = SESSION_DIR / session_id
    if json_file.exists():
        json_file.unlink()
    if folder.exists():
        import shutil
        shutil.rmtree(folder)
    return {"success": True}


@app.post("/api/chat")
async def chat(req: ChatRequest):
    """
    多轮对话终点：
    - 有 session_id → 继续收集信息或生成推荐
    - 无 session_id → 视为新消息，返回引导
    """
    sid = req.session_id
    user_msg = req.message.strip()

    # 无 session → 提示创建会话
    if not sid or sid not in _sessions:
        # 简单回复引导创建会话
        pois = search_nearby_pois(req.lat, req.lng)
        poi_text = "\n".join(
            f"- {p['name']}（{p.get('type','')}，距你{p.get('distance','')}米）"
            for p in pois[:6]
        ) if pois else "暂无附近数据"

        system = (
            "你是旅行助手。用户还没开始正式的行程规划。请根据附近POI信息给出简短有趣的建议，"
            "并引导用户告诉你：目的地、日期、住宿位置、行程时长。回复要简短，不超过150字。"
        )
        user = f"用户位置（{req.lat},{req.lng}）。附近地点：\n{poi_text}\n\n用户说：{user_msg}"
        reply = call_deepseek(system, user) or f"收到！我看到你附近有一些不错的地方。想去哪里？什么时候出发？告诉我你的计划，我来帮你安排。"

        return {"type": "message", "content": reply, "session_id": None}

    session = _sessions[sid]

    # 收集信息阶段
    if session["state"] == "collecting":
        step = session["step"]
        key = STEPS[step]
        session["inputs"][key] = user_msg
        session["messages"].append({"role": "user", "content": user_msg})

        # 智能检测：从输入中提取时长
        for k, v in TOUR_DURATIONS.items():
            if k in user_msg:
                session["inputs"]["duration"] = v
                break

        # 智能检测：从输入中提取日期
        date_match = re.search(r"(\d{1,2}月\d{1,2}[日号])|(下周[一二三四五六日天])|(明天|后天|今天)", user_msg)
        if date_match:
            session["inputs"]["date"] = date_match.group(0)

        # 跳过已收集的步骤
        next_step = step + 1
        while next_step < len(STEPS) and session["inputs"].get(STEPS[next_step]):
            next_step += 1

        # 检查是否全部收集完毕
        all_done = all(session["inputs"].get(s) for s in STEPS)

        if all_done:
            # 全部信息已收集，进入确认状态
            session["state"] = "confirming"
            inp = session["inputs"]
            dur_label = ""
            for k, v in TOUR_DURATIONS.items():
                if v == inp["duration"] and len(k) <= 3:
                    dur_label = k + "游"
                    break
            reply = (
                f"收到！为您确认以下信息：\n\n"
                f"📍 目的地：{inp['destination']}\n"
                f"📅 日期：{inp['date']}\n"
                f"🏨 居住位置：{inp['residence']}\n"
                f"⏱️ 行程时长：{dur_label or inp['duration']}\n\n"
                f"确认无误请回复「确认」或「好的」，或告诉我需要调整的部分。"
            )
        elif next_step >= len(STEPS):
            # 跳过了但没全齐（不应出现），继续生成
            session["state"] = "generating"
            session["messages"].append({
                "role": "assistant",
                "content": "信息收集完毕！正在为你查询天气、周边景点和旅行攻略..."
            })
            _save_session(sid)
            try:
                result = _generate_recommendation(session)
                session["result"] = result
                session["state"] = "done"
                reply = result.get("summary", "推荐生成完成！")
            except Exception as e:
                reply = f"推荐生成时出错：{e}"
                session["state"] = "collecting"
                session["step"] = step
                session["inputs"][key] = None
        else:
            session["step"] = next_step
            session["state"] = "collecting"
            next_key = STEPS[next_step]
            reply = STEP_PROMPTS[next_key]

        session["messages"].append({"role": "assistant", "content": reply})
        _save_session(sid)
        return {
            "type": "message",
            "content": reply,
            "session_id": sid,
            "state": session["state"],
            "current_step": STEPS[session["step"]] if session["step"] < len(STEPS) else ""
        }

    # 确认阶段：等待用户确认
    if session["state"] == "confirming":
        session["messages"].append({"role": "user", "content": user_msg})

        if re.search(r"确认|好的|可以|没问题|行|ok|yes|对|没错|嗯", user_msg, re.IGNORECASE):
            # 用户确认，开始生成
            session["state"] = "generating"
            session["messages"].append({
                "role": "assistant",
                "content": "好的，正在为你查询天气、周边景点和旅行攻略..."
            })
            _save_session(sid)
            try:
                result = _generate_recommendation(session)
                session["result"] = result
                session["state"] = "done"
                reply = result.get("summary", "推荐生成完成！")
            except Exception as e:
                reply = f"推荐生成时出错：{e}"
                session["state"] = "confirming"
        else:
            # 用户想调整，回到 collecting 状态
            session["state"] = "collecting"
            session["step"] = 0
            reply = "好的，请告诉我你想调整什么？是目的地、日期、住宿还是行程时长？"

        session["messages"].append({"role": "assistant", "content": reply})
        _save_session(sid)
        return {
            "type": "message",
            "content": reply,
            "session_id": sid,
            "state": session["state"],
            "current_step": STEPS[0] if session["state"] == "collecting" else ""
        }

    # 推荐已完成，后续对话
    if session["state"] == "done":
        session["messages"].append({"role": "user", "content": user_msg})

        result = session.get("result", {})
        weather_text = json.dumps(result.get("weather", {}), ensure_ascii=False)[:500] if result.get("weather") else "暂无天气数据"

        system = (
            "你是旅行助手，推荐已生成。请基于已有的推荐结果回答用户后续问题。"
            "回复要简短、贴近年轻人、有趣。如果在150字内可以完成就不要超出。"
        )
        user = f"现有推荐：\n景点：{json.dumps(result.get('attractions', []), ensure_ascii=False)[:500]}\n\n"
        user += f"购物：{json.dumps(result.get('shopping', []), ensure_ascii=False)[:300]}\n\n"
        user += f"装备建议：\n{json.dumps(result.get('gear', []), ensure_ascii=False)[:300]}\n\n"
        user += f"装备建议：\n{json.dumps(result.get('gear', []), ensure_ascii=False)[:300]}\n\n"
        user += f"天气：{weather_text}\n\n用户说：{user_msg}"

        reply = call_deepseek(system, user) or "收到你的消息了！有什么需要调整的吗？"
        session["messages"].append({"role": "assistant", "content": reply})
        _save_session(sid)
        return {
            "type": "message",
            "content": reply,
            "session_id": sid,
            "state": session["state"],
            "route_plan": (session.get("result") or {}).get("route_plan"),
        }

    return {"type": "message", "content": "正在处理...", "session_id": sid, "state": session.get("state")}


def _generate_recommendation(session: dict) -> dict:
    """收集完信息后的推荐生成核心逻辑"""
    inp = session["inputs"]
    dest = inp["destination"] or ""
    date = inp["date"] or ""
    residence = inp["residence"] or ""
    duration = inp["duration"] or "1-day"

    # 1. 地理编码获取目的地坐标
    coords = geocode_city(dest)
    if not coords:
        # 尝试用居住地坐标
        coords = geocode_city(residence) or (31.2304, 121.4737)

    # 2. 搜索周边POI
    pois = search_nearby_pois(coords[0], coords[1])

    # 3. 查询天气
    weather = get_weather(dest, date)

    # 4. Zhihu搜索
    zhihu = search_zhihu(f"{dest} 旅游攻略")

    # 5. 装备推荐
    poi_types = [p.get("type", "") for p in pois[:20]]
    terrain_tags = []
    type_keywords = {
        "山": "山区", "森林": "森林", "湖": "湖边", "海": "海边",
        "沙滩": "沙滩", "丛林": "丛林", "漂流": "水上", "湿地": "湖边"
    }
    for pt in poi_types:
        for kw, tag in type_keywords.items():
            if kw in pt:
                terrain_tags.append(tag)
    terrain_tags = list(set(terrain_tags))
    gear = recommend_gear(weather, terrain_tags)

    # 6. 分类 POI 并构建结构化数据
    attractions = []
    shopping = []
    _attraction_types = {"风景名胜", "公园", "博物馆", "展览馆", "寺庙", "教堂", "海滩",
                         "山", "岛", "古镇", "园林", "纪念馆", "植物园", "动物园",
                         "观光点", "国家级景点", "省级景点", "游乐园", "水上活动中心"}
    _shopping_types = {"购物中心", "商场", "便利店", "超市", "专卖店", "市场",
                       "商业街", "步行街", "百货", "商铺"}

    def _parse_coords(loc_str: str):
        """高德location格式: 'lng,lat' → (lat, lng)"""
        if not loc_str or "," not in loc_str:
            return None, None
        parts = loc_str.split(",")
        try:
            return float(parts[1]), float(parts[0])
        except (ValueError, IndexError):
            return None, None

    def _guess_shopping_products(name: str, amap_type: str) -> list[str]:
        """根据店铺名称/类型推荐可购买商品"""
        name_type = name + amap_type
        products = []
        if any(kw in name_type for kw in ["纪念品", "礼品", "特产", "手信"]):
            products.append("当地特产/纪念品")
        if any(kw in name_type for kw in ["服饰", "服装", "衣", "鞋", "帽"]):
            products.append("服装鞋帽")
        if any(kw in name_type for kw in ["户外", "运动", "露营", "登山", "渔具"]):
            products.append("户外运动装备")
        if any(kw in name_type for kw in ["数码", "电子", "手机", "电脑"]):
            products.append("数码电子产品")
        if any(kw in name_type for kw in ["食品", "零食", "糕点", "糖果", "茶叶"]):
            products.append("食品/零食")
        if any(kw in name_type for kw in ["美妆", "护肤", "化妆品", "香水"]):
            products.append("美妆护肤品")
        if any(kw in name_type for kw in ["书店", "图书", "文具"]):
            products.append("书籍文具")
        if any(kw in name_type for kw in ["药", "保健", "药妆"]):
            products.append("药品保健品")
        if any(kw in name_type for kw in ["珠宝", "首饰", "手表", "眼镜"]):
            products.append("珠宝配饰")
        if any(kw in name_type for kw in ["家居", "家具", "家纺", "厨具"]):
            products.append("家居用品")
        if any(kw in name_type for kw in ["母婴", "儿童", "玩具"]):
            products.append("母婴儿童用品")
        if any(kw in name_type for kw in ["花", "宠物", "园艺"]):
            products.append("花卉宠物用品")
        if any(kw in name_type for kw in ["咖啡", "奶茶", "饮品", "茶"]):
            products.append("饮品/茶叶")
        if not products:
            products.append("日用百货")
        return products

    for p in pois[:30]:
        lat, lng = _parse_coords(p.get("location", ""))
        name = p.get("name", "")
        amap_type = p.get("type", "")
        item = {
            "name": name,
            "type": amap_type,
            "address": p.get("address", ""),
            "distance": p.get("distance", "0"),
            "lat": lat,
            "lng": lng,
            "crs": "GCJ-02",
            "rating": p.get("rating", ""),
        }
        is_shop = (any(kw in amap_type for kw in _shopping_types) or
                   any(kw in amap_type for kw in ["购物", "店", "商场", "超市", "市场"]))
        if is_shop:
            item["recommended_products"] = _guess_shopping_products(name, amap_type)
            shopping.append(item)
        else:
            attractions.append(item)

    # 7. 构建推荐 Prompt
    duration_label = {v: k for k, v in TOUR_DURATIONS.items()}.get(duration, "一日游")
    for k, v in TOUR_DURATIONS.items():
        if v == duration and len(k) <= 3:
            duration_label = k + "游"
            break

    poi_text = "\n".join(
        f"{i+1}. {p['name']}（{p.get('type','')}，距目标{p.get('distance','')}米，评分{p.get('rating','?')}）"
        for i, p in enumerate(pois[:20])
    )

    shopping_text = "\n".join(
        f"{i+1}. {s['name']}\n   地址：{s.get('address','')}\n   推荐商品：{', '.join(s.get('recommended_products', []))}"
        for i, s in enumerate(shopping[:10])
    ) if shopping else "暂无周边购物数据"

    zhihu_text = "\n".join(
        f"- [{z['title']}]({z['url']})\n  {z['snippet']}"
        for z in zhihu
    )

    weather_summary = "暂无天气数据"
    if weather and weather.get("daily"):
        t = weather["daily"][0]
        weather_summary = (
            f"{weather['city']} {t['date']}：{t['text_day']}，{t['temp_min']}°C ~ {t['temp_max']}°C，"
            f"风力{t.get('wind_scale','?')}级，湿度{t.get('humidity','?')}% ，UV指数{t.get('uv_index','?')}"
        )

    gear_text = "\n".join(
        f"- {g['icon']} {g['name']}：{g['reason']}"
        for g in gear
    ) if gear else "暂无特殊装备建议"

    # 行程点数建议
    if duration == "half-day":
        spot_guide = "推荐 1 个核心景点或一组相邻景点（2-3个），停留时间 3-4 小时"
    elif duration == "1-day":
        spot_guide = "推荐 4-6 个景点，合理排列路线，每个点标注停留时间"
    else:
        spot_guide = "安排每日行程（每天3-4个景点），按天分列，标注每段交通方式"

    # 读取模板文件
    try:
        prompt_template = (DIALOG_DIR / "prompt.md").read_text(encoding="utf-8")
    except Exception:
        prompt_template = ""
    try:
        output_template = (DIALOG_DIR / "output.md").read_text(encoding="utf-8")
    except Exception:
        output_template = ""

    # System prompt 是模板的第一段（到第一个 ## 之前）
    system = prompt_template.split("##")[0].strip() if prompt_template else (
        "你是一个潮流的 AI 旅伴助手，为年轻人设计个性化旅行方案。"
        "你的风格：有趣、接地气、知道年轻人的痛点（拍照好看、性价比高、小众不踩雷）。"
        "回复要详细但不过长，用口语化风格。"
    )

    # User prompt = prompt 模板的变量部分 + output 模板
    user = prompt_template.replace(system, "").strip() if prompt_template else ""
    user = user.replace("{dest}", dest)
    user = user.replace("{date}", date)
    user = user.replace("{residence}", residence)
    user = user.replace("{duration_label}", duration_label)
    user = user.replace("{weather_summary}", weather_summary)
    user = user.replace("{poi_text}", poi_text)
    user = user.replace("{shopping_text}", shopping_text)
    user = user.replace("{zhihu_text}", zhihu_text)
    user = user.replace("{gear_text}", gear_text)
    user = user.replace("{spot_guide}", spot_guide)

    # 拼接 output 模板
    user += "\n\n" + output_template.replace("{spot_guide}", spot_guide)

    full_reply = call_deepseek(system, user)
    if not full_reply:
        full_reply = f"## {dest} {duration_label} 推荐\n\n根据你的需求，我为你准备了以下推荐...\n\n{poi_text[:500]}"

    # 构建结构化返回结果：分拆景点和购物，包含完整坐标
    attractions = []
    shopping = []
    _attraction_types = {"风景名胜", "公园", "博物馆", "展览馆", "寺庙", "教堂", "海滩",
                         "山", "岛", "古镇", "园林", "纪念馆", "植物园", "动物园",
                         "观光点", "国家级景点", "省级景点", "游乐园", "水上活动中心"}
    _shopping_types = {"购物中心", "商场", "便利店", "超市", "专卖店", "市场",
                       "商业街", "步行街", "百货", "商铺"}

    def _parse_coords(loc_str: str):
        """高德location格式: 'lng,lat' → (lat, lng)"""
        if not loc_str or "," not in loc_str:
            return None, None
        parts = loc_str.split(",")
        try:
            return float(parts[1]), float(parts[0])
        except (ValueError, IndexError):
            return None, None

    def _guess_shopping_products(name: str, amap_type: str) -> list[str]:
        """根据店铺名称/类型推荐可购买商品"""
        name_type = name + amap_type
        products = []
        if any(kw in name_type for kw in ["纪念品", "礼品", "特产", "手信"]):
            products.append("当地特产/纪念品")
        if any(kw in name_type for kw in ["服饰", "服装", "衣", "鞋", "帽"]):
            products.append("服装鞋帽")
        if any(kw in name_type for kw in ["户外", "运动", "露营", "登山", "渔具"]):
            products.append("户外运动装备")
        if any(kw in name_type for kw in ["数码", "电子", "手机", "电脑"]):
            products.append("数码电子产品")
        if any(kw in name_type for kw in ["食品", "零食", "糕点", "糖果", "茶叶"]):
            products.append("食品/零食")
        if any(kw in name_type for kw in ["美妆", "护肤", "化妆品", "香水"]):
            products.append("美妆护肤品")
        if any(kw in name_type for kw in ["书店", "图书", "文具"]):
            products.append("书籍文具")
        if any(kw in name_type for kw in ["药", "保健", "药妆"]):
            products.append("药品保健品")
        if any(kw in name_type for kw in ["珠宝", "首饰", "手表", "眼镜"]):
            products.append("珠宝配饰")
        if any(kw in name_type for kw in ["家居", "家具", "家纺", "厨具"]):
            products.append("家居用品")
        if any(kw in name_type for kw in ["母婴", "儿童", "玩具"]):
            products.append("母婴儿童用品")
        if any(kw in name_type for kw in ["花", "宠物", "园艺"]):
            products.append("花卉宠物用品")
        if any(kw in name_type for kw in ["咖啡", "奶茶", "饮品", "茶"]):
            products.append("饮品/茶叶")
        if not products:
            products.append("日用百货")
        return products

    for p in pois[:20]:
        lat, lng = _parse_coords(p.get("location", ""))
        name = p.get("name", "")
        amap_type = p.get("type", "")
        item = {
            "name": name,
            "type": amap_type,
            "address": p.get("address", ""),
            "distance": p.get("distance", "0"),
            "lat": lat,
            "lng": lng,
            "crs": "GCJ-02",
            "rating": p.get("rating", ""),
        }
        # 分类
        is_shop = (any(kw in amap_type for kw in _shopping_types) or
                   any(kw in amap_type for kw in ["购物", "店", "商场", "超市", "市场"]))
        if is_shop:
            item["recommended_products"] = _guess_shopping_products(name, amap_type)
            shopping.append(item)
        else:
            attractions.append(item)

    route_plan = build_route_plan_from_text(full_reply, attractions, duration)

    return {
        "summary": full_reply,
        "attractions": attractions,
        "route_plan": route_plan,
        "shopping": shopping,
        "weather": weather,
        "zhihu": zhihu,
        "gear": gear,
        "destination_coords": {"lat": coords[0], "lng": coords[1], "crs": "WGS-84"},
    }


# ===== Auth (mock) =====
_FAKE_TOKEN = "dev-token-12345"
_FAKE_USER_ID = 1
_verification_codes: dict[str, str] = {}
_cart: list[dict] = []


class SendCodeRequest(BaseModel):
    phone: str


class LoginRequest(BaseModel):
    phone: str
    code: str


@app.post("/api/auth/send-code")
async def send_code(req: SendCodeRequest):
    code = "123456"
    _verification_codes[req.phone] = code
    return {"success": True, "message": "验证码已发送（开发模式：123456）"}


@app.post("/api/auth/login")
async def login(req: LoginRequest):
    if req.code == "123456":
        return {"token": _FAKE_TOKEN, "user_id": _FAKE_USER_ID}
    stored = _verification_codes.get(req.phone)
    if stored and stored == req.code:
        return {"token": _FAKE_TOKEN, "user_id": _FAKE_USER_ID}
    return {"detail": "验证码错误"}


@app.get("/api/user/profile")
async def get_profile():
    return {"id": _FAKE_USER_ID, "phone": "138****8888", "nickname": "旅行者", "avatar_url": ""}


# ===== Tours =====
@app.get("/api/tours")
async def list_tours(lat: float = 31.2304, lng: float = 121.4737, duration: str = "1-day"):
    pois = search_nearby_pois(lat, lng)
    return [
        {"id": i + 1, "title": p["name"], "duration": duration,
         "description": f"{p.get('type','')} · 距你{p.get('distance','')}米 — {p.get('address','')}",
         "favorites_count": random.randint(50, 500)}
        for i, p in enumerate(pois[:8])
    ]


# ===== Products =====
@app.get("/api/products")
async def search_products(lat: float = 31.2304, lng: float = 121.4737):
    pois = search_nearby_pois(lat, lng, radius=3000)
    shops = [p for p in pois if "购物" in p.get("type", "") or "店" in p.get("name", "")]
    if not shops:
        shops = pois[:8]
    return [
        {"id": i + 1, "name": s["name"], "price": random.randint(20, 200),
         "shop_name": s["name"], "image": "", "product_url": "",
         "reason": "来自附近的好物推荐"}
        for i, s in enumerate(shops[:8])
    ]


@app.post("/api/products/ai-recommend")
async def ai_recommend(lat: float = 31.2304, lng: float = 121.4737):
    return await search_products(lat, lng)


# ===== Cart & Orders (mock) =====
class AddCartRequest(BaseModel):
    product_name: str
    product_image: str = ""
    product_url: str = ""
    price: float = 0
    quantity: int = 1
    shop_name: str = ""


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


@app.get("/api/cart")
async def list_cart():
    return _cart


@app.post("/api/cart")
async def add_to_cart(req: AddCartRequest):
    item = req.model_dump()
    item["id"] = random.randint(100, 999)
    _cart.append(item)
    return item


@app.delete("/api/cart/{item_id}")
async def remove_cart_item(item_id: int):
    global _cart
    _cart = [i for i in _cart if i.get("id") != item_id]
    return {"success": True}


@app.post("/api/orders/quick")
async def quick_order(req: QuickOrderRequest):
    order_no = "TA" + "".join(random.choices("0123456789", k=14))
    return {"success": True, "order_no": order_no, "total_amount": req.price * req.quantity}


@app.get("/api/orders")
async def list_orders():
    return []
