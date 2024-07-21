from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Shop  # Импортируем модель Shop из models.py
from crud import get_all_cities, get_streets_by_city, create_shop, get_shops  # Импортируем функции из crud.py
from database import SessionLocal, init_db  # Импортируем из database.py
import schemas  # Импортируем схемы из schemas.py
from typing import List

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

async def get_db():
    async with SessionLocal() as db:
        yield db

@app.get("/city/", response_model=List[schemas.City])
async def read_cities(db: AsyncSession = Depends(get_db)):
    cities = await get_all_cities(db)
    return cities

@app.get("/city/{city_id}/street/", response_model=List[schemas.Street])
async def read_streets(city_id: int, db: AsyncSession = Depends(get_db)):
    streets = await get_streets_by_city(db, city_id)
    return streets

@app.post("/shop/", response_model=schemas.Shop)
async def create_new_shop(shop: schemas.ShopCreate, db: AsyncSession = Depends(get_db)):
    new_shop = await create_shop(db, Shop(**shop.dict()))
    return new_shop

@app.get("/shop/", response_model=List[schemas.Shop])
async def read_shops(city_id: int = None, street_id: int = None, open: int = None, db: AsyncSession = Depends(get_db)):
    shops = await get_shops(db, city_id, street_id, open)
    return shops