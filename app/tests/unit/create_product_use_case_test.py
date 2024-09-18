import pytest

from app.tests.utils import create_product
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyProductDescriptionError,
    EmptyProductNameError,
    EmptyProductThumbnailError,
    InvalidProductPriceError,
    NegativeStockError,
    NonPositiveWeightError,
)
from app.use_cases.products.create_product_use_case import CreateProductUseCase


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
        name="Valid Name",
        thumbnail="https://example.com/thumbnail.png",
        description="Valid description",
        stock=10,
        weight=1.0,
        brand="Valid Brand",
    )
    with pytest.raises(InvalidProductPriceError):
        await create_product_use_case(invalid_product)

    invalid_product.price = 100
    invalid_product.name = ""
    with pytest.raises(EmptyProductNameError):
        await create_product_use_case(invalid_product)

    invalid_product.name = "Valid Name"
    invalid_product.thumbnail = ""
    with pytest.raises(EmptyProductThumbnailError):
        await create_product_use_case(invalid_product)

    invalid_product.thumbnail = "https://example.com/thumbnail.png"
    invalid_product.description = ""
    with pytest.raises(EmptyProductDescriptionError):
        await create_product_use_case(invalid_product)

    invalid_product.description = "Valid description"
    invalid_product.brand = ""
    with pytest.raises(EmptyBrandError):
        await create_product_use_case(invalid_product)

    invalid_product.brand = "Valid Brand"
    invalid_product.stock = -1
    with pytest.raises(NegativeStockError):
        await create_product_use_case(invalid_product)
