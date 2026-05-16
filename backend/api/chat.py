import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from .deps import decode_access_token

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active: dict[int, WebSocket] = {}

    async def connect(self, user_id: int, ws: WebSocket):
        await ws.accept()
        self.active[user_id] = ws

    def disconnect(self, user_id: int):
        self.active.pop(user_id, None)

    async def send(self, user_id: int, message: str):
        ws = self.active.get(user_id)
        if ws:
            await ws.send_text(message)


manager = ConnectionManager()


@router.websocket("/ws/chat")
async def chat_websocket(websocket: WebSocket):
    token = websocket.query_params.get("token", "")
    user_id = decode_access_token(token)
    if user_id is None:
        await websocket.close(code=4001)
        return

    await manager.connect(user_id, websocket)
    await manager.send(user_id, json.dumps({"type": "welcome", "message": "你好！我是你的 AI 旅伴助手，有什么可以帮你的？"}))

    try:
        while True:
            data = await websocket.receive_text()
            msg = json.loads(data)
            user_message = msg.get("message", "")

            # TODO: integrate LangGraph Agent for real AI response
            reply = _mock_ai_reply(user_message)
            await manager.send(user_id, json.dumps({"type": "message", "content": reply}))
    except WebSocketDisconnect:
        manager.disconnect(user_id)


def _mock_ai_reply(message: str) -> str:
    if "行程" in message or "计划" in message:
        return "好的，我来帮你调整行程。请问你想修改哪一天的安排？"
    if "购物" in message or "买" in message:
        return "我来帮你看看有什么合适的伴手礼。你想要什么类型的商品？"
    if "推荐" in message:
        return "根据你的位置，我推荐以下景点：故宫（2.5km）、天坛（3.1km）、北海公园（1.8km）。你对哪个感兴趣？"
    return f"收到你的消息了。让我想想怎么帮你……（你说了：{message}）"
