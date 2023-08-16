from typing import List

from pydantic import BaseModel

class Inventory(BaseModel):
    FechaInventario: str
    GLN_Cliente: str
    GLN_sucursal: str
    Gtin_Producto: str
    Inventario_Final: int
    PrecioUnidad: float
class InventoryResponse(BaseModel):
    inventarios: List[Inventory]
    total: int
