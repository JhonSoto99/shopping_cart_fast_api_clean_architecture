from app.domain.enitities.item import Product
from app.ports.repositories.product_repository import ProductRepository
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyProductDescriptionError,
    EmptyProductNameError,
    EmptyProductThumbnailError,
    InvalidProductPriceError,
    NegativeStockError,
    NonPositiveWeightError,
)


class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    async def __call__(self, product: Product) -> None:
        if product.price <= 0:
            raise InvalidProductPriceError()

        if not product.name:
            raise EmptyProductNameError()

        if not product.thumbnail:
            raise EmptyProductThumbnailError()

        if not product.description:
            raise EmptyProductDescriptionError()

        if product.stock < 0:
            raise NegativeStockError()

        if product.weight <= 0:
            raise NonPositiveWeightError()

        if not product.brand:
            raise EmptyBrandError()

        await self._product_repository.add(product)
