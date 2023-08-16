from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Inventario(Base):
    __tablename__ = 'inventario'

    id = Column(Integer, primary_key=True, index=True)
    fechainventario = Column(Date, nullable=False)
    id_sucursal = Column(Integer)
    id_producto = Column(Integer)
    inventario_final = Column(Integer)
    preciounidad = Column(Float)

