from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth import router as auth_router
from .tour import router as tour_router
from .product import router as product_router
from .order import router as order_router
from .chat import router as chat_router
from .location import router as location_router

app = FastAPI(title="Touring Advisor AI", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(tour_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(chat_router)
app.include_router(location_router)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/plan")
async def plan():
    # Legacy SSE endpoint stub - to be implemented with LangGraph
    return {"message": "SSE streaming not yet implemented"}
