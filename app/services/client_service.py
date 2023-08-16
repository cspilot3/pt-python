from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.utils.utils import validate_flush


def get_or_create_cliente(db: Session, gln_cliente: str):
    cliente = db.query(Cliente).filter_by(gln_cliente=gln_cliente).first()
    if not cliente:
        cliente = Cliente(gln_cliente=gln_cliente, nombre="Cliente Desconocido")
        db.add(cliente)
        validate_flush(db)
    return cliente

def get_gln_cliente(db: Session, id: int):
    client = db.query(Cliente).filter(Cliente.id == id).first()
    res = client.gln_cliente if client else None
    return res