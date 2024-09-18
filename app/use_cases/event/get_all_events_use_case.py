from typing import List

from app.drivers.rest.routers.schema import EventOutput
from app.ports.repositories.event_repository import EventRepository


class GetAllEventsUseCase:
    def __init__(self, event_repository: EventRepository):
        self._event_repository = event_repository

    async def __call__(self) -> List[EventOutput]:
        return await self._event_repository.get_all()
