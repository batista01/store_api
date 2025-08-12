from fastapi import Query
from app.schemas import ProductFilter, ProductOut
from typing import List

@router.get("/products", response_model=List[ProductOut])
async def list_products(
    price_min: Optional[Decimal] = Query(None, description="Minimum price"),
    price_max: Optional[Decimal] = Query(None, description="Maximum price"),
):
    filters = ProductFilter(price_min=price_min, price_max=price_max)
    return await product_service.list(filters)
