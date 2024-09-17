from abc import ABC, abstractmethod
from typing import List

from app.domain.enitities.item import Event
from app.drivers.rest.routers.schema import EventOutput


class EventRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[EventOutput]:
        pass

    @abstractmethod
    async def add(self, product: Event) -> bool:
        pass
