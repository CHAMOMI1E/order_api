from fastapi import APIRouter, Depends
from app.db.models.base import db_session
from app.db.requests.order import create_order, get_order_by_id, get_orders, update_order_status
from app.schemas.order import OrderCreate, OrderStatusUpdate
from sqlalchemy.orm import Session 


order_router = APIRouter()


@order_router.post("/")
async def create_order_endpoint(model: OrderCreate, db: Session=Depends(db_session)):
    result = await create_order(model=model, session=db)
    return result


@order_router.get("/")
async def get_orders_endpoint(db: Session=Depends(db_session)):
    result = await get_orders(session=db)
    return result


@order_router.get("/{id}")
async def get_order_by_id_endpoint(id: int, db: Session=Depends(db_session)):
    result = await get_order_by_id(session=db, order_id=id)
    return result


@order_router.patch("/{id}/status")
async def update_order_status_endpoint(id: int, model: OrderStatusUpdate, db: Session=Depends(db_session)):
    result = await update_order_status(order_id=id, new_status=model.status, session=db)
    return result
