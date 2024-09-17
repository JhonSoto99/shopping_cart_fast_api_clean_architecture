from abc import ABC, abstractmethod
from typing import Any, List

from app.domain.enitities.item import Product
from app.drivers.rest.routers.schema import ProductOutput


class ProductRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[ProductOutput]:
        pass

    @abstractmethod
    async def add(self, product: Product) -> bool:
        pass
