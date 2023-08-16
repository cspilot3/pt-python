from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.services.branch_service import get_gln_cliente_from_suc, get_gln_sucursal
from app.services.product_service import get_gtin_producto


Base = declarative_base()

class Inventario(Base):
    __tablename__ = 'inventario'

    id = Column(Integer, primary_key=True, index=True)
    fechainventario = Column(Date, nullable=False)
    id_sucursal = Column(Integer)
    id_producto = Column(Integer)
    inventario_final = Column(Integer)
    preciounidad = Column(Float)

    def serialize(self, db: Session):

        return {
            'fechainventario': str(self.fechainventario),
            'gln_cliente': get_gln_cliente_from_suc(db, self.id_sucursal),
            'gln_sucursal': get_gln_sucursal(db, self.id_sucursal),
            'gtin_producto': get_gtin_producto(db, self.id_producto),
            'inventario_final': self.inventario_final,
            'preciounidad': self.preciounidad
        }

