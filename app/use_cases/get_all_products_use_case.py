from typing import List

from app.domain.enitities.item import Product
from app.drivers.rest.routers.schema import ProductOutput
from app.ports.repositories.product_repository import ProductRepository


class GetAllProductsUseCase:
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    async def __call__(self) -> List[ProductOutput]:
        return await self._product_repository.get_all()
