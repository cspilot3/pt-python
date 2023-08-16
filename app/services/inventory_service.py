from fastapi import File, UploadFile, status
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from app.utils.utils import get_gln_cliente_from_upload_file, validate_flush, apply_changes
from app.services.blob_service import upload_file_to_blob_storage, move_blob_to_processed_folder
from app.services.client_service import get_or_create_cliente
from app.services.branch_service import get_or_create_sucursal
from app.services.product_service import get_or_create_producto
from datetime import datetime

from app.models.inventario import Inventario


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