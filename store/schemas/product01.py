from typing import Optional
from pydantic import Field
from decimal import Decimal
from store.schemas.base import BaseSchemaMixin


class ProductFilter(BaseSchemaMixin):
    price_min: Optional[Decimal] = Field(None, description="Minimum price")
    price_max: Optional[Decimal] = Field(None, description="Maximum price")
