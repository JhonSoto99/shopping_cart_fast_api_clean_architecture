import pytest

from app.ports.repositories.product_repository import ProductRepository
from app.tests.utils import create_product
from app.use_cases.create_product_use_case import CreateProductUseCase
from app.use_cases.products.get_all_products_use_case import (
    GetAllProductsUseCase,
)


@pytest.fixture
def get_all_products_use_case(
    products_repository: ProductRepository,
) -> GetAllProductsUseCase:
    return GetAllProductsUseCase(products_repository)


@pytest.mark.asyncio
async def test_get_all_products_success(
    get_all_products_use_case: GetAllProductsUseCase,
    create_product_use_case: CreateProductUseCase,
):
    product1 = create_product()
    product2 = create_product()
    await create_product_use_case(product1)
    await create_product_use_case(product2)
    products = await get_all_products_use_case()
    assert len(products) == 2


@pytest.mark.asyncio
async def test_get_all_products_empty(
    get_all_products_use_case: GetAllProductsUseCase,
):
    products = await get_all_products_use_case()
    assert products == []
