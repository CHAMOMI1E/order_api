from sqlalchemy import Float
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.base import Base


class Product(Base):
    __tablename__ = "product"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    price: Mapped[float] = mapped_column(nullable=False)
    stock: Mapped[int] = mapped_column(nullable=False)
