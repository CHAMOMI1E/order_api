import asyncio
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.models.base import db_session
from app.db.requests.product import delete_product, get_product_by_id, get_products, create_product, update_product
from app.schemas.product import ProductCreate, ProductUpdate


product_router = APIRouter()


@product_router.post("/")
async def add_products(model: ProductCreate, db: Session=Depends(db_session)):

    product = await create_product(
        session=db,
        model=model,
    )
    return product


@product_router.get("/")
async def get_products_endpoint(db: Session=Depends(db_session)):
    products = await get_products(session=db)
    return products


@product_router.get("/{id}")
async def get_product_by_id_endpoint(id, db: Session=Depends(db_session)):
    product = await get_product_by_id(session=db, product_id=int(id))
    return product


@product_router.put("/{id}")
async def update_product_endpoint(id: int, model: ProductUpdate, db: Session=Depends(db_session)):
    result = await update_product(session=db, product_id=id, model=model)
    return result


@product_router.delete("/{id}")
async def delete_product_endpoint(id: int, db: Session=Depends(db_session)):
    result = await delete_product(session=db, product_id=id)
    return result



