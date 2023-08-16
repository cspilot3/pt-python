from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, index=True)
    gln_cliente = Column(String, unique=True, index=True, nullable=False)
    nombre = Column(String, nullable=False)

