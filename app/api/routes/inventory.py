from fastapi import APIRouter, HTTPException, Depends, status, Query
from fastapi import UploadFile, File
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.inventory_service import process_inventory
from app.utils.utils import count_records_in_file
from fastapi.responses import JSONResponse
from app.models.schemas.Inventory import InventoryResponse
from app.models.inventario import Inventario
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

@router.get("/inventories/", 
            response_model=InventoryResponse
            )
def get_inventories(
    page: int = Query(1, description="Número de página"),
    items_per_page: int = Query(10, description="Cantidad de elementos por página"),
    db: Session = Depends(get_db),
):
    try:
        inventories_query: Query = db.query(Inventario).filter().all()
        total = len(inventories_query)
        start_index = (page - 1) * items_per_page
        end_index = start_index + items_per_page
        inventories = inventories_query[start_index : end_index]
        inventories = [inventory.serialize(db) for inventory in inventories]

        return InventoryResponse(inventarios=inventories, total=total)
    except Exception as e:
        return JSONResponse(content={"message": f"{str(e)}"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)