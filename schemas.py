
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Literal

# Şemaları net tutmak, API'nin ne beklediğini açık eder.

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    price_cents: int = Field(ge=0)
    stock_qty: int = Field(ge=0)

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price_cents: Optional[int] = Field(default=None, ge=0)
    stock_qty: Optional[int] = Field(default=None, ge=0)

class ProductOut(BaseModel):
    id: int
    name: str
    price_cents: int
    stock_qty: int
    class Config:
        from_attributes = True

class OrderItemIn(BaseModel):
    product_id: int
    quantity: int = Field(ge=1)

class OrderCreate(BaseModel):
    user_id: int
    items: List[OrderItemIn]

class OrderOutItem(BaseModel):
    product_id: int
    quantity: int
    unit_price_cents: int
    class Config:
        from_attributes = True

class OrderOut(BaseModel):
    id: int
    user_id: int
    status: Literal["PENDING","PAID","CANCELLED"]
    total_cents: int
    items: List[OrderOutItem]
    class Config:
        from_attributes = True
