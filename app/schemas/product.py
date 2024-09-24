from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int = Field(..., gt=0)


class ProductCreate(ProductBase):
    pass

    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductList(BaseModel):
    products: List[Product]

    class Config:
        orm_mode = True
