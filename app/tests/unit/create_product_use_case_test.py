import pytest

from app.adapters.repositories.product_repository.in_memory_repository import (
    InMemoryProductRepository,
)
from app.ports.repositories.product_repository import ProductRepository
from app.tests.utils import create_product
from app.use_cases.create_product_use_case import CreateProductUseCase
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyProductNameError,
    InvalidProductPriceError,
    NegativeStockError,
    NonPositiveWeightError,
)


@pytest.fixture
def products_repository() -> ProductRepository:
    return InMemoryProductRepository()


@pytest.fixture
def create_product_use_case(
    products_repository: ProductRepository,
) -> CreateProductUseCase:
    return CreateProductUseCase(products_repository)


@pytest.mark.asyncio
async def test_add_valid_product(create_product_use_case: CreateProductUseCase):
    product = create_product()
    await create_product_use_case(product)


@pytest.mark.asyncio
async def test_add_invalid_product(
    create_product_use_case: CreateProductUseCase,
):
    invalid_product = create_product(
        price=-100,
        name="",
        thumbnail="",
        description="",
        stock=-1,
        weight=0.0,
        brand="",
    )

    with pytest.raises(InvalidProductPriceError):
        await create_product_use_case(invalid_product)

    invalid_product.price = 100
    with pytest.raises(EmptyProductNameError):
        await create_product_use_case(invalid_product)

    invalid_product.name = "Producto válido"
    with pytest.raises(NegativeStockError):
        await create_product_use_case(invalid_product)

    invalid_product.stock = 10
    with pytest.raises(NonPositiveWeightError):
        await create_product_use_case(invalid_product)

    invalid_product.weight = 1.0
    with pytest.raises(EmptyBrandError):
        await create_product_use_case(invalid_product)
