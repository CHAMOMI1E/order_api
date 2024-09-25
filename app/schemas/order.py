from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class OrderItemBase(BaseModel):
    product_id: int
    stock: int = Field(..., gt=0)


class OrderItemCreate(OrderItemBase):
    pass

class OrderBase(BaseModel):
    status: Optional[str] = "в процессе"


class OrderCreate(OrderBase):
    items: List[OrderItemCreate]


class OrderStatusUpdate(BaseModel):
    status: Literal["в процессе", "отправлен", "доставлен"]
