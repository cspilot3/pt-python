from fastapi import File, UploadFile, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.utils.utils import get_gln_cliente_from_upload_file, validate_flush, apply_changes
from app.services.blob_service import upload_file_to_blob_storage, move_blob_to_processed_folder
from datetime import datetime

from app.models import (Cliente, Sucursal, Producto, Inventario)


def get_or_create_cliente(db: Session, gln_cliente: str):
    cliente = db.query(Cliente).filter_by(gln_cliente=gln_cliente).first()
    if not cliente:
        cliente = Cliente(gln_cliente=gln_cliente, nombre="Cliente Desconocido")
        db.add(cliente)
        validate_flush(db)
    return cliente

def get_or_create_sucursal(db: Session, gln_sucursal: str, cliente_id: int):
    sucursal = db.query(Sucursal).filter_by(gln_sucursal=gln_sucursal, id_cliente=cliente_id).first()
    if not sucursal:
        sucursal = Sucursal(gln_sucursal=gln_sucursal, nombre="Sucursal Desconocida", id_cliente=cliente_id)
        db.add(sucursal)
        validate_flush(db)
    return sucursal

def get_or_create_producto(db: Session, gtn_producto: str):
    producto = db.query(Producto).filter_by(gtin_producto=gtn_producto).first()
    if not producto:
        producto = Producto(gtin_producto=gtn_producto, nombre="Producto Desconocido")
        db.add(producto)
        validate_flush(db)
    return producto

async def process_record(db: Session, gln_cliente: str, record: str):
    fields = record.split(",")
    fecha_inventario_str = fields[0]
    fecha_inventario = datetime.strptime(fecha_inventario_str, "%d/%m/%Y").date()
    gln_sucursal = fields[2]
    gtn_producto = fields[3]
    inventario_final = int(fields[4])
    precio_unidad = float(fields[5])
    
    cliente = get_or_create_cliente(db, gln_cliente)
    sucursal = get_or_create_sucursal(db, gln_sucursal, cliente.id)
    producto = get_or_create_producto(db, gtn_producto)

    nuevo_inventario = Inventario(
        fechainventario=fecha_inventario,
        id_sucursal=sucursal.id,
        id_producto=producto.id,
        inventario_final=inventario_final,
        preciounidad=precio_unidad
    )
    db.add(nuevo_inventario)

    validate_flush(db)

async def process_inventory(file: UploadFile, db: Session):
        gln_cliente = get_gln_cliente_from_upload_file(file)
        if gln_cliente is not None:
            upload_successful, msj = upload_file_to_blob_storage(file, gln_cliente)
            if not upload_successful:
                raise Exception(msj)

            file.file.seek(0)
            content = file.file.read().decode('utf-8')
            lines = content.split("\n")
            for line in lines[1:]:
                if line.strip():
                    await process_record(db, gln_cliente, line)
            apply_changes(db)
            move_blob_to_processed_folder(file.filename, gln_cliente)

        else:
            raise Exception("Error al procesar el archivo")