from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.drivers.rest.dependencies import get_created_product_use_case
from app.drivers.rest.routers.schema import ProductInput
from app.use_cases.create_product_use_case import CreateProductUseCase
from app.use_cases.exceptions import InvalidProductPriceError

router = APIRouter(prefix="/products")


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def create_product(
    data: ProductInput,
    use_case: Annotated[
        CreateProductUseCase, Depends(get_created_product_use_case)
    ],
) -> None:
    await use_case(data.to_entity())


@router.post("/", status_code=status.HTTP_204_NO_CONTENT)
async def ger_products(
    use_case: Annotated[
        CreateProductUseCase, Depends(get_created_product_use_case)
    ],
) -> None:
    await use_case(data.to_entity())
