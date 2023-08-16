from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = 'producto'

    id = Column(Integer, primary_key=True, index=True)
    gtin_producto = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)

