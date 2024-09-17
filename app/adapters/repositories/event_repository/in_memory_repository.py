from typing import Any
from typing import List
from uuid import UUID

from app.domain.enitities.item import Event
from app.ports.repositories.event_repository import EventRepository


class InMemoryEventRepository(EventRepository):
    events: List[Event] = []

    async def get(self, **filters: Any) -> Event | None:
        for event in self.events:
            if (f := filters.get("id")) and f == event.id:
                return event
        return None

    def clear(self):
        self.events = []

    async def get_by_id(self, event_id: UUID) -> Event:
        return next((event for event in self.events if event.id == event_id), None)


    async def get_all(self) -> List[Event]:
        return self.events

    async def add(self, event: Event) -> bool:
        self.events.append(event)
        return True
