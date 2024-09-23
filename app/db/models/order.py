from datetime import datetime
from enum import Enum
from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.models.base import Base
from app.db.models.product import Product


class Order(Base):
    __tablename__ = "order"

    created_date: Mapped[datetime] = mapped_column(default=datetime.now, nullable=False)
    status: Mapped[Enum] = mapped_column(
        Enum("в процессе", "отправлен", "доставлен", name="order_status"),
        nullable=False,
    )
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_item"

    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)

    order: Mapped["Order"] = relationship(back_populates="order_items")
    product: Mapped["Product"] = relationship()
