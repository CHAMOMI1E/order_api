from sqlalchemy import insert, update, delete, select
from app.db import Product, db_session
from app.schemas.product import ProductCreate


async def create_product(
    session: db_session, 
    model: ProductCreate
):
    try:
        product = await session.execute(
            insert(Product)
            .values(**model.dict())            
            .returning(Product.id, Product.name, Product.description, Product.price, Product.stock)
        )
        return {"message": "Product created successfully"}
    except Exception as e:
        print(e)
        return {"message": "Product creation failed"}


async def get_products(session: db_session):
    query = select(Product)
    result = await session.execute(query)
    return result.fetchall()


async def get_product_by_id(session: db_session, product_id: int) -> Product:
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.fetchone()


async def get_product_by_id(session: db_session, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.fetchone()


async def update_product(session: db_session, product_id: int, stock: int):
    try:
        product = await get_product_by_id(session=session, product_id=product_id)
        if product.stock >= stock:
            result = await session.execute(
                update(Product).where(Product.id == product_id).values(stock=stock)
            )
            print(result)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


async def delete_product(session: db_session, product_id: int):
    try:
        query = delete(Product).where(Product.id == product_id)
        result = await session.execute(query)
        return True
    except Exception as e:
        return False
