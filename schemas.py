from pydantic import BaseModel
from typing import List, Optional

class CityBase(BaseModel):
    name: str

class City(CityBase):
    id: int
    streets: List['Street'] = []

    class Config:
        orm_mode = True

class StreetBase(BaseModel):
    name: str
    city_id: int

class Street(StreetBase):
    id: int
    city: City

    class Config:
        orm_mode = True

class ShopBase(BaseModel):
    name: str
    city_id: int
    street_id: int
    house: str
    open_time: str
    close_time: str

class ShopCreate(ShopBase):
    pass

class Shop(ShopBase):
    id: int
    city: City
    street: Street

    class Config:
        orm_mode = True