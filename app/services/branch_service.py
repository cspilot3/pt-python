from sqlalchemy.orm import Session
from app.models.sucursal import Sucursal
from app.utils.utils import validate_flush
from app.services.client_service import get_gln_cliente


def get_or_create_sucursal(db: Session, gln_sucursal: str, cliente_id: int):
    sucursal = db.query(Sucursal).filter_by(gln_sucursal=gln_sucursal, id_cliente=cliente_id).first()
    if not sucursal:
        sucursal = Sucursal(gln_sucursal=gln_sucursal, nombre="Sucursal Desconocida", id_cliente=cliente_id)
        db.add(sucursal)
        validate_flush(db)
    return sucursal

def get_gln_cliente_from_suc(db: Session, id: int):
    suc = db.query(Sucursal).filter(Sucursal.id == id).first()
    gln_cliente = get_gln_cliente(db, suc.id_cliente) if suc else None
    return gln_cliente

def get_gln_sucursal(db: Session, id: int):
    suc = db.query(Sucursal).filter(Sucursal.id == id).first()
    res = suc.gln_sucursal if suc else None
    return res