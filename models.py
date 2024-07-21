from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Time

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    streets = relationship("Street", back_populates="city")
    shops = relationship("Shop", back_populates="city")


class Street(Base):
    __tablename__ = 'streets'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))

    city = relationship("City", back_populates="streets")
    shops = relationship("Shop", back_populates="street")


class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    street_id = Column(Integer, ForeignKey('streets.id'))
    house = Column(String)
    open_time = Column(Time)
    close_time = Column(Time)

    city = relationship("City", back_populates="shops")
    street = relationship("Street", back_populates="shops")