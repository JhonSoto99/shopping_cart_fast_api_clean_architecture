from abc import ABC, abstractmethod
from typing import Any, List
from uuid import UUID

from app.domain.enitities.cart import CartItem
from app.domain.enitities.item import Event
from app.drivers.rest.routers.schema import EventOutput


class EventRepository(ABC):
    @abstractmethod
    async def update_stock(
        self, event_id: UUID, new_stock: int
    ) -> CartItem | None:
        pass

    @abstractmethod
    async def get(self, **filters: Any) -> CartItem | None:
        pass

    @abstractmethod
    async def get_all(self) -> List[EventOutput]:
        pass

    @abstractmethod
    async def add(self, product: Event) -> bool:
        pass
