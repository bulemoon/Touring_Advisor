"""
AI 旅伴助手 — 开发入口
定位 → AMap POI 搜周边 5km → Kimi LLM 生成年轻人视角推荐
"""
import os
import json
import random
from dotenv import load_dotenv
import requests
from fastapi import FastAPI
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
KIMI_KEY = os.getenv("KIMI_API_KEY", "")
ZHIHU_SECRET = os.getenv("ZHIHU_ACCESS_SECRET", "")

# ===== AMap POI Search (5km radius) =====
_AMAP_CACHE: dict[str, list[dict]] = {}

def search_nearby_pois(lat: float, lng: float, radius: int = 5000) -> list[dict]:
    cache_key = f"{lat:.4f},{lng:.4f},{radius}"
    if cache_key in _AMAP_CACHE:
        return _AMAP_CACHE[cache_key]

    # Search multiple POI types
    types_list = [
        "060000",  # 旅游景点
        "050000",  # 餐饮
        "070000",  # 购物
        "110000",  # 休闲娱乐
    ]
    all_pois = []
    for t in types_list:
        try:
            r = requests.get(
                "https://restapi.amap.com/v3/place/around",
                params={
                    "key": AMAP_KEY,
                    "location": f"{lng},{lat}",
                    "radius": radius,
                    "types": t,
                    "offset": 10,
                    "page": 1,
                    "extensions": "all",
                },
                timeout=5,
            )
            data = r.json()
            if data.get("status") == "1":
                pois = data.get("pois", [])
                for p in pois:
                    all_pois.append({
                        "name": p.get("name", ""),
                        "type": p.get("type", ""),
                        "address": p.get("address", ""),
                        "distance": p.get("distance", "0"),
                        "location": p.get("location", ""),
                        "biz_ext": p.get("biz_ext", {}),
                    })
        except Exception as e:
            print(f"[AMap] Error searching type {t}: {e}")

    # Deduplicate by name
    seen = set()
    unique = []
    for p in all_pois:
        if p["name"] not in seen:
            seen.add(p["name"])
            unique.append(p)

    _AMAP_CACHE[cache_key] = unique
    return unique


# ===== Zhihu Search =====
_ZHIHU_CACHE: dict[str, list[dict]] = {}

def search_zhihu(query: str) -> list[dict]:
    if query in _ZHIHU_CACHE:
        return _ZHIHU_CACHE[query]
    results = []
    try:
        r = requests.post(
            "https://openapi.zhihu.com/v3/search",
            headers={
                "Authorization": f"Bearer {ZHIHU_SECRET}",
                "Content-Type": "application/json",
            },
            json={"q": query, "limit": 5},
            timeout=5,
        )
        data = r.json()
        for item in data.get("data", []):
            results.append({
                "title": item.get("title", ""),
                "snippet": item.get("snippet", ""),
                "url": item.get("url", ""),
            })
    except Exception as e:
        print(f"[Zhihu] Search error: {e}")
    _ZHIHU_CACHE[query] = results
    return results


# ===== Kimi LLM =====
def call_kimi(system: str, user: str) -> str:
    try:
        r = requests.post(
            "https://api.moonshot.cn/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {KIMI_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "moonshot-v1-8k",
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "temperature": 0.8,
                "max_tokens": 2000,
            },
            timeout=30,
        )
        data = r.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"[Kimi] Error: {e}")
        return ""


# ===== Agent: Tour Recommendations =====
_TOUR_DURATIONS = {
    "half-day": "半日游（3-4小时）",
    "1-day": "一日游（6-8小时）",
    "3-day": "三日游（每天6-8小时）",
}

def agent_recommend_tours(lat: float, lng: float, duration: str) -> list[dict]:
    pois = search_nearby_pois(lat, lng)
    if not pois:
        return _fallback_tours(lat, lng, duration)

    poi_text = "\n".join(
        f"{i+1}. {p['name']}（{p['type']}，距你{p['distance']}米）"
        for i, p in enumerate(pois[:15])
    )

    duration_label = _TOUR_DURATIONS.get(duration, "一日游")
    prompt = (
        f"我在当前位置（{lat},{lng}），附近有以下地点：\n{poi_text}\n\n"
        f"请以年轻人视角设计一个{duration_label}的旅行路线方案。\n"
        f"要求：\n"
        f"1. 从上面列表中选取合适的景点/地点\n"
        f"2. 按合理顺序排列，给出每个点建议停留时间\n"
        f"3. 每个点写一句年轻人喜欢的推荐语（有趣、接地气）\n"
        f"4. 路线要顺路，不要来回跑\n"
        f"5. 如果是半日游则3-4个点，一日游5-7个点，三日游每天3-4个点\n"
        f"6. 附上整个路线的总预估时间和交通建议\n\n"
        f"请用 JSON 格式返回，格式：\n"
        f'[{{\"title\":\"路线标题\", \"stops\":[{{\"name\":\"地点名\", \"duration_min\":分钟数, \"tip\":\"推荐语\"}}], \"total_min\":总分钟数, \"transport\":\"交通建议\"}}]'
    )

    system = (
        "你是一个潮流的 AI 旅伴助手，为年轻人设计旅行路线。"
        "你的风格：有趣、接地气、知道年轻人的痛点（拍照好看、性价比高、小众不踩雷）。"
        "严格按照 JSON 格式返回，不要加 markdown 代码块标记。"
    )

    result = call_kimi(system, prompt)
    try:
        parsed = json.loads(result)
        for route in parsed:
            route["id"] = random.randint(100, 999)
            route["duration"] = duration
            route["description"] = f"全程约{route.get('total_min', 0)}分钟，{route.get('transport', '')}"
            route["favorites_count"] = random.randint(50, 500)
        return parsed
    except (json.JSONDecodeError, TypeError):
        pass

    return _fallback_tours(lat, lng, duration)


def _fallback_tours(lat: float, lng: float, duration: str) -> list[dict]:
    pois = search_nearby_pois(lat, lng)[:5]
    if not pois:
        return [{"id": 1, "title": "探索你所在的城市", "duration": duration,
                  "description": "开启你的城市探索之旅", "favorites_count": 99}]
    tours = []
    for i, p in enumerate(pois):
        tours.append({
            "id": i + 1,
            "title": p["name"],
            "duration": duration,
            "description": f"{p['type']} · 距你{p['distance']}米 — {p['address']}",
            "favorites_count": random.randint(50, 500),
        })
    return tours


# ===== Agent: Product Recommendations =====
def agent_recommend_products(lat: float, lng: float) -> list[dict]:
    pois = search_nearby_pois(lat, lng, radius=3000)
    shops = [p for p in pois if "购物" in p.get("type", "") or "商场" in p.get("name", "") or "店" in p.get("name", "")]

    if not shops:
        shops = pois[:8]

    if not shops:
        return _fallback_products()

    shop_text = "\n".join(
        f"{i+1}. {s['name']}（{s.get('type','')}，距你{s.get('distance','')}米）"
        for i, s in enumerate(shops[:8])
    )

    prompt = (
        f"我在当前位置（{lat},{lng}），附近有以下商家：\n{shop_text}\n\n"
        f"请以年轻人视角推荐适合作为伴手礼/纪念品的商品。\n"
        f"要求：\n"
        f"1. 从附近商家中推荐具体商品\n"
        f"2. 每件商品写一句年轻人喜欢的推荐理由（要潮、有趣）\n"
        f"3. 价格适中（20-200元之间）\n"
        f"4. 适合送朋友或有特色的本地好物\n\n"
        f"请用 JSON 格式返回，格式：\n"
        f'[{{\"name\":\"商品名\", \"price\":价格(数字), \"shop_name\":\"店名\", \"reason\":\"推荐理由\"}}]'
    )

    system = (
        "你是一个懂年轻人品味的购物推荐助手。"
        "推荐的伴手礼要满足：颜值高、有趣、实用、价格不贵。"
        "严格按照 JSON 格式返回，不要加 markdown 代码块标记。"
    )

    result = call_kimi(system, prompt)
    try:
        parsed = json.loads(result)
        for i, item in enumerate(parsed):
            item["id"] = i + 1
            item["image"] = ""
            item["product_url"] = ""
        return parsed
    except (json.JSONDecodeError, TypeError):
        pass

    return _fallback_products()


def _fallback_products() -> list[dict]:
    return [
        {"id": 1, "name": "城市限定帆布包", "price": 68, "shop_name": "本地文创店",
         "image": "", "product_url": "", "reason": "背着它你就是这条街最靓的仔"},
        {"id": 2, "name": "手工特色冰箱贴", "price": 28, "shop_name": "礼品店",
         "image": "", "product_url": "", "reason": "旅行打卡纪念，送朋友不踩雷"},
    ]


# ===== Auth (mock) =====
_FAKE_TOKEN = "dev-token-12345"
_FAKE_USER_ID = 1
_verification_codes: dict[str, str] = {}


class SendCodeRequest(BaseModel):
    phone: str


class LoginRequest(BaseModel):
    phone: str
    code: str


@app.post("/api/auth/send-code")
async def send_code(req: SendCodeRequest):
    code = "123456"
    _verification_codes[req.phone] = code
    print(f"[Dev] Code for {req.phone}: {code}")
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


# ===== AI Chat (HTTP POST, no WebSocket needed) =====
class ChatRequest(BaseModel):
    message: str
    lat: float = 31.2304
    lng: float = 121.4737


@app.post("/api/chat")
async def chat(req: ChatRequest):
    pois = search_nearby_pois(req.lat, req.lng)
    poi_text = "\n".join(
        f"{i+1}. {p['name']}（{p.get('type','')}，距你{p.get('distance','')}米）"
        for i, p in enumerate(pois[:10])
    ) if pois else "附近暂无数据"

    system = (
        "你是一个潮流的 AI 旅伴助手，擅长帮年轻人规划旅行和购物。"
        "回复要简短有趣、接地气，用年轻人的口吻。"
        "如果你需要修改行程或购物车，在回复末尾加上操作标记。"
    )
    user = f"我在当前位置（{req.lat},{req.lng}），附近有：\n{poi_text}\n\n用户说：{req.message}"

    reply = call_kimi(system, user)
    if not reply:
        reply = f"收到你的消息了！我来帮你看看附近有什么好玩的。（你说：{req.message}）"

    return {"type": "message", "content": reply}


@app.get("/api/chat/history")
async def chat_history():
    return {"messages": []}


# ===== API Endpoints =====
@app.get("/api/tours")
async def list_tours(lat: float = 31.2304, lng: float = 121.4737, duration: str = "1-day"):
    tours = agent_recommend_tours(lat, lng, duration)
    return tours


@app.get("/api/products")
async def search_products(lat: float = 31.2304, lng: float = 121.4737):
    return agent_recommend_products(lat, lng)


@app.post("/api/products/ai-recommend")
async def ai_recommend(lat: float = 31.2304, lng: float = 121.4737):
    return agent_recommend_products(lat, lng)


# ===== Cart & Orders (mock) =====
_cart: list[dict] = []


class AddCartRequest(BaseModel):
    product_name: str
    product_image: str = ""
    product_url: str = ""
    price: float = 0
    quantity: int = 1
    shop_name: str = ""


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


@app.post("/api/orders/quick")
async def quick_order(req: QuickOrderRequest):
    order_no = "TA" + "".join(random.choices("0123456789", k=14))
    return {"success": True, "order_no": order_no, "total_amount": req.price * req.quantity}


@app.get("/api/orders")
async def list_orders():
    return []


@app.get("/health")
async def health():
    return {"status": "ok", "mode": "agent"}
