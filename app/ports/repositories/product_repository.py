from abc import ABC, abstractmethod
from typing import Any

from app.domain.enitities.item import Product


class ProductRepository(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> Product | None:
        pass

    @abstractmethod
    async def add(self, product: Product) -> bool:
        pass
