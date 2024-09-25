from typing import Literal
from sqlalchemy import insert, update, select
from sqlalchemy.exc import NoResultFound
from app.db import Order, OrderItem, db_session
from app.db.models.product import Product
from app.db.requests.product import get_product_by_id
from app.schemas.order import OrderCreate


async def create_order(session: db_session, model: OrderCreate):
    try:
        new_order = await session.execute(
            insert(Order).values(status=model.status).returning(Order.id)
        )

        new_order_id = new_order.scalar_one()

        for item in model.items:

            result = await session.execute(
                select(Product).where(Product.id == item.product_id)
            )
            product = result.scalar_one_or_none()

            if product is None:
                raise ValueError(f"Product with ID {item.product_id} not found")

            requested_quantity = item.stock
            available_stock = product.stock

            if requested_quantity > available_stock:
                raise ValueError(
                    f"Requested quantity ({requested_quantity}) exceeds available stock ({available_stock}) for product {item.product_id}"
                )

            await session.execute(
                update(Product)
                .where(Product.id == item.product_id)
                .values(stock=available_stock - requested_quantity)
            )

            await session.execute(
                insert(OrderItem).values(
                    order_id=new_order_id,
                    product_id=item.product_id,
                    quantity=requested_quantity,
                )
            )

        await session.commit()

        return {"message": "Order created successfully", "order_id": new_order_id}

    except NoResultFound:
        await session.rollback()
        return {"message": "Product not found"}

    except Exception as e:
        await session.rollback()
        return {"message": f"Order creation failed: {e}"}


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


async def update_order_status(
    order_id: int,
    new_status: Literal["в процессе", "отправлен", "доставлен"],
    session: db_session,
):
    try:
        result = await session.execute(
            update(Order).where(id == order_id).values(status=new_status)
        )
        return True
    except Exception as e:
        return False
