from sqlalchemy import insert, update, delete, select
from app.db import Product, db_session


async def create_product(session: db_session, name: str, description: str, price: float, stock: int):
    try:
        query = insert(Product).values(name=name, description=description, price=price, stock=stock)
        result = await session.execute(query)
        return True
    except Exception as e:
        return False
    

async def get_products(session: db_session):
    query = select(Product)
    result = await session.execute(query)
    return result.fetchall()


async def get_product_by_id(session: db_session, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.fetchone()


async def update_product(session: db_session, **kwargs):
    try:
        query = update(Product).where(Product.id == kwargs['id']).values(**kwargs)
        result = await session.execute(query)
        return True
    except Exception as e:
        return False
    

async def delete_product(session: db_session, product_id: int):
    try:
        query = delete(Product).where(Product.id == product_id)
        result = await session.execute(query)
        return True
    except Exception as e:
        return False