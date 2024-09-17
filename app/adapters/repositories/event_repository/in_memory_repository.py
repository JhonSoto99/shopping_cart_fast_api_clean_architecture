from typing import List

from app.domain.enitities.item import Event
from app.ports.repositories.event_repository import EventRepository


class InMemoryEventRepository(EventRepository):
    events: List[Event] = []

    def clear(self):
        self.events = []

    async def get_all(self) -> List[Event]:
        return self.events

    async def add(self, event: Event) -> bool:
        self.events.append(event)
        return True
