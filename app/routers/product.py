from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.models.base import db_session
from app.db.requests.product import get_products, create_product
from app.schemas.product import ProductCreate


product_router = APIRouter()


@product_router.post("/")
async def add_products(model: ProductCreate, db=Depends(db_session)):

    product = await create_product(
        session=db,
        model=model,
    )
    return product


@product_router.get("/")
async def get_product_by_id(session: db_session):
    products = await get_products


@product_router.get("/{id}")
async def get_product_by_id(id):
    pass


@product_router.put("/{id}")
async def update_product(id):
    pass


@product_router.delete("/{id}")
async def delete_product(id):
    pass
