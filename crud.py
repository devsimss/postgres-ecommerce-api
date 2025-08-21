
from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas

# İş mantığını endpointlerden ayrı tutmak, test etmeyi ve geliştirmeyi kolaylaştırır.

def create_user(db: Session, data: schemas.UserCreate) -> models.User:
    u = models.User(email=data.email, full_name=data.full_name)
    db.add(u)
    db.commit()
    db.refresh(u)
    return u

def get_user(db: Session, user_id: int):
    return db.get(models.User, user_id)

def create_product(db: Session, data: schemas.ProductCreate) -> models.Product:
    p = models.Product(name=data.name, price_cents=data.price_cents, stock_qty=data.stock_qty)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p

def list_products(db: Session):
    return list(db.scalars(select(models.Product).order_by(models.Product.id)))

def update_product(db: Session, product_id: int, data: schemas.ProductUpdate):
    p = db.get(models.Product, product_id)
    if not p:
        return None
    if data.name is not None:
        p.name = data.name
    if data.price_cents is not None:
        p.price_cents = data.price_cents
    if data.stock_qty is not None:
        p.stock_qty = data.stock_qty
    db.commit()
    db.refresh(p)
    return p

def create_order(db: Session, data: schemas.OrderCreate) -> models.Order:
    user = db.get(models.User, data.user_id)
    if not user:
        raise ValueError("User not found")

    order = models.Order(user_id=user.id, status=models.OrderStatus.PENDING, total_cents=0)
    db.add(order)
    db.flush()  # id lazım

    total = 0
    for it in data.items:
        prod = db.get(models.Product, it.product_id)
        if not prod:
            raise ValueError(f"Product {it.product_id} not found")
        if prod.stock_qty < it.quantity:
            raise ValueError(f"Insufficient stock for product {prod.id}")
        unit = prod.price_cents
        total += unit * it.quantity
        prod.stock_qty -= it.quantity  
        db.add(models.OrderItem(order_id=order.id, product_id=prod.id, quantity=it.quantity, unit_price_cents=unit))

    order.total_cents = total
    db.commit()
    db.refresh(order)
    return order

def get_order(db: Session, order_id: int):
    return db.get(models.Order, order_id)

def mark_paid(db: Session, order_id: int):
    o = db.get(models.Order, order_id)
    if not o:
        return None
    o.status = models.OrderStatus.PAID
    db.commit()
    db.refresh(o)
    return o
