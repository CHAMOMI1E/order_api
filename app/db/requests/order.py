from typing import Literal
from sqlalchemy import insert, update, delete, select
from app.db import Order, db_session


async def create_order(product_id: int, quantity: int, session: db_session):
    try:
        result = await session.execute(
            insert(Order).values(product_id=product_id, quantity=quantity)
        )
        return True
    except Exception as e:
        return False


async def get_orders(session: db_session):
    try:
        result = await session.execute(select(Order))
        orders = result.fetchall()
        return orders
    except Exception as e:
        return None
    

async def get_order_by_id(session: db_session, order_id: int):
    try:
        result = await session.execute(select(Order).where(Order.id == order_id))
        order = result.fetchone()
        return order
    except Exception as e:
        return None
    

async def update_order_status(order_id: int, new_status: Literal["в процессе", "отправлен", "доставлен"], session: db_session):
    try:
        result = await session.execute(
            update(Order).where(id == order_id).values(status=new_status)
        )
        session.commit()
        return True
    except Exception as e:
        return False