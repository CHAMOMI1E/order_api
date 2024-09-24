from fastapi import APIRouter
from app.schemas.order import *


order_router = APIRouter()


@order_router.post("/")
async def create_order():
    pass


@order_router.get("/")
async def get_order():
    pass


@order_router.get("/{id}", response_model=OrderStatusUpdate)
async def get_order_by_id(id: int):
    pass


@order_router.patch("/{id}/status")
async def update_order_status(model: OrderBase, id: int):
    return {"message": "done"}
