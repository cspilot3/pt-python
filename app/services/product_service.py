from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.utils.utils import validate_flush


def get_or_create_producto(db: Session, gtn_producto: str):
    producto = db.query(Producto).filter_by(gtin_producto=gtn_producto).first()
    if not producto:
        producto = Producto(gtin_producto=gtn_producto, nombre="Producto Desconocido")
        db.add(producto)
        validate_flush(db)
    return producto

def get_gtin_producto(db: Session, id: int):
    prod = db.query(Producto).filter(Producto.id == id).first()
    res = prod.gtin_producto if prod else None
    return res