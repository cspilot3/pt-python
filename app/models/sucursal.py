from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
# from .cliente import Cliente

Base = declarative_base()

class Sucursal(Base):
    __tablename__ = 'sucursal'

    id = Column(Integer, primary_key=True, index=True)
    gln_sucursal = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    id_cliente = Column(Integer)
