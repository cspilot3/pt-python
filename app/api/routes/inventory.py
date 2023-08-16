from fastapi import APIRouter, HTTPException, Depends, status, Query
from fastapi import UploadFile, File
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.blob_service import upload_file_to_blob_storage
from app.services.inventory_service import process_inventory
from app.utils.utils import get_gln_cliente_from_upload_file, count_records_in_file
from fastapi.responses import JSONResponse
from app.models.schemas.Inventory import InventoryResponse
from app.models import Inventario, Sucursal, Cliente
from typing import List, Optional
import asyncio

router = APIRouter()

@router.post(
    "/inventories/",
    status_code=status.HTTP_201_CREATED,
)
async def upload_inventory(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    try:
        num_records = count_records_in_file(file)
        if num_records <= 100000:
            await process_inventory(file, db)
            return JSONResponse(content={"message": "Procesamiento completado"}, status_code=status.HTTP_200_OK)
        else:
            asyncio.create_task(process_inventory(file, db))
            return JSONResponse(content={"message": "Procesamiento en segundo plano iniciado"}, status_code=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return JSONResponse(content={"message": f"{str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
