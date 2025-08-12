from fastapi import APIRouter, HTTPException
from sqlalchemy.exc import IntegrityError
from app.schemas import ProductCreate, ProductResponse
from app.services import product_service
from app.repositories.exceptions import ProductAlreadyExistsException

router = APIRouter()


@router.post("/products", response_model=ProductResponse, status_code=201)
async def create_product(product: ProductCreate):
    try:
        return await product_service.create(product)
    except ProductAlreadyExistsException:
        raise HTTPException(
            status_code=400,
            detail="A product with the same name already exists."
        )
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Failed to insert product due to a database integrity error."
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error while creating product."
        )
