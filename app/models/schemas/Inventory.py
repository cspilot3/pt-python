from typing import List

from pydantic import BaseModel

class Inventory(BaseModel):
    fechainventario: str
    gln_cliente: str
    gln_sucursal: str
    gtin_producto: str
    inventario_final: int
    preciounidad: float
class InventoryResponse(BaseModel):
    inventarios: List[Inventory]
    total: int
