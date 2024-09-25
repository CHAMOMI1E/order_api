from fastapi import APIRouter, Depends
from app.db.models.base import db_session
from app.db.requests.order import create_order
from app.schemas.order import OrderBase, OrderCreate, OrderStatusUpdate
from sqlalchemy.orm import Session 


order_router = APIRouter()


@order_router.post("/")
async def create_order_endpoint(model: OrderCreate, db: Session=Depends(db_session)):
    result = await create_order(model=model, session=db)
    return result


@order_router.get("/")
async def get_orders_endpoint():
    pass


@order_router.get("/{id}", response_model=OrderStatusUpdate)
async def get_order_by_id_endpoint(id: int):
    pass


@order_router.patch("/{id}/status")
async def update_order_status_endpoint(model: OrderBase, id: int):
    return {"message": "done"}
