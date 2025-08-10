
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import crud, schemas

app = FastAPI(title="E‑Commerce API", version="0.2.0")

@app.on_event("startup")
def init_db():
    # Demo için tabloyu burada oluşturuyoruz. Migrationsız hız kazandırıyor.
    Base.metadata.create_all(bind=engine)

@app.post("/users", response_model=schemas.UserOut, status_code=201)
def users_create(data: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, data)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def users_get(user_id: int, db: Session = Depends(get_db)):
    u = crud.get_user(db, user_id)
    if not u:
        raise HTTPException(404, "User not found")
    return u

@app.post("/products", response_model=schemas.ProductOut, status_code=201)
def products_create(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, data)

@app.get("/products", response_model=list[schemas.ProductOut])
def products_list(db: Session = Depends(get_db)):
    return crud.list_products(db)

@app.patch("/products/{product_id}", response_model=schemas.ProductOut)
def products_update(product_id: int, data: schemas.ProductUpdate, db: Session = Depends(get_db)):
    p = crud.update_product(db, product_id, data)
    if not p:
        raise HTTPException(404, "Product not found")
    return p

@app.post("/orders", response_model=schemas.OrderOut, status_code=201)
def orders_create(data: schemas.OrderCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_order(db, data)
    except ValueError as e:
        raise HTTPException(400, str(e))

@app.get("/orders/{order_id}", response_model=schemas.OrderOut)
def orders_get(order_id: int, db: Session = Depends(get_db)):
    o = crud.get_order(db, order_id)
    if not o:
        raise HTTPException(404, "Order not found")
    return o

@app.post("/orders/{order_id}/pay", response_model=schemas.OrderOut)
def orders_pay(order_id: int, db: Session = Depends(get_db)):
    o = crud.mark_paid(db, order_id)
    if not o:
        raise HTTPException(404, "Order not found")
    return o
