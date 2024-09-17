from typing import Any, List
from uuid import UUID

from app.domain.enitities.item import Event
from app.ports.repositories.event_repository import EventRepository


class InMemoryEventRepository(EventRepository):
    events: List[Event] = []

    async def update_stock(self, event_id: UUID, new_stock: int):
        for event in self.events:
            if event.id == event_id:
                event.stock = new_stock
                return

    async def get(self, **filters: Any) -> Event | None:
        for event in self.events:
            if (f := filters.get("id")) and f == event.id:
                return event
        return None

    def clear(self):
        self.events = []

    async def get_all(self) -> List[Event]:
        return self.events

    async def add(self, event: Event) -> bool:
        self.events.append(event)
        return True
