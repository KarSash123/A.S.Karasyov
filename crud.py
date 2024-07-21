from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import City, Street, Shop  # Импортируем модели из models.py

async def get_all_cities(db: AsyncSession):
    result = await db.execute(select(City))
    return result.scalars().all()

async def get_streets_by_city(db: AsyncSession, city_id: int):
    result = await db.execute(select(Street).where(Street.city_id == city_id))
    return result.scalars().all()

async def create_shop(db: AsyncSession, shop: Shop):
    db.add(shop)
    await db.commit()
    await db.refresh(shop)
    return shop

async def get_shops(db: AsyncSession, city_id: int = None, street_id: int = None, open: bool = None):
    query = select(Shop)
    if city_id:
        query = query.where(Shop.city_id == city_id)
    if street_id:
        query = query.where(Shop.street_id == street_id)
    if open is not None:
        # Here should be implemented the open/close time logic
        pass
    result = await db.execute(query)
    return result.scalars().all()