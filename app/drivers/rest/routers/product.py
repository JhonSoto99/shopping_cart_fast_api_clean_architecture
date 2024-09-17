from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.drivers.rest.dependencies import (
    get_all_products_use_case,
    get_created_product_use_case,
)
from app.drivers.rest.routers.schema import ProductCreate, ProductOutput
from app.use_cases.create_product_use_case import CreateProductUseCase
from app.use_cases.get_all_products_use_case import GetAllProductsUseCase

router = APIRouter(prefix="/products")


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def create_product(
    data: ProductCreate,
    use_case: Annotated[
        CreateProductUseCase, Depends(get_created_product_use_case)
    ],
) -> None:
    await use_case(data.to_entity())


@router.get(
    "/", response_model=List[ProductOutput], status_code=status.HTTP_200_OK
)
async def get_products(
    use_case: Annotated[
        GetAllProductsUseCase, Depends(get_all_products_use_case)
    ],
) -> List[ProductOutput]:
    products = await use_case()
    return products
