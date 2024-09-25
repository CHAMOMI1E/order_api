from sqlalchemy import insert, update, delete, select
from app.db import Product, db_session
from app.schemas.product import ProductCreate, ProductUpdate
from dataclasses import asdict



async def create_product(
    session: db_session, 
    model: ProductCreate
):
    try:
        product = await session.execute(
            insert(Product)
            .values(**model.dict())            
        )
        await session.commit()
        return {"message": "Product created successfully"}
    except Exception as e:
        print(e)
        return {"error": "Product creation failed"}


async def get_products(session: db_session):
    products_query = await session.execute(select(Product))
    products = products_query.scalars().all()
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock
        })
    return result


async def get_product_by_id(session: db_session, product_id: int) -> dict:
    query = select(Product).where(Product.id == product_id)
    product = (await session.execute(query)).scalar_one()
    return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock
        }



async def update_product(session: db_session, product_id: int, model: ProductUpdate):
    try:
        final_model: dict = {}
        for key, value in model.dict().items():
            if value is not None:
                final_model[key] = value
        product = await session.execute(
                                        update(Product)
                                        .where(Product.id == product_id)
                                        .values(**final_model)
                                        )
        await session.commit()
        return {"message": "Product updated successfully"}
    except Exception as e:
        print(e)
        return {"error": "Product updated failed"}


async def delete_product(session: db_session, product_id: int):
    try:
        query = delete(Product).where(Product.id == product_id)
        result = await session.execute(query)
        await session.commit()
        return {"message": "Product deleted successfully"}
    except Exception as e:
        return {"error": "Product deleted  failed"}