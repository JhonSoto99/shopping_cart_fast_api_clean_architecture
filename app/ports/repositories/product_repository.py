from abc import ABC, abstractmethod
from typing import Any, List
from uuid import UUID

from app.domain.enitities.cart import CartItem
from app.domain.enitities.item import Product
from app.drivers.rest.routers.schema import ProductOutput


class ProductRepository(ABC):
    @abstractmethod
    async def get(self, **filters: Any) -> CartItem | None:
        pass

    @abstractmethod
    async def get_all(self) -> List[ProductOutput]:
        pass

    @abstractmethod
    async def get_by_id(self, event_id: UUID) -> CartItem:
        pass

    @abstractmethod
    async def add(self, product: Product) -> bool:
        pass
