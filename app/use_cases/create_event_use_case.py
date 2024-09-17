from app.domain.enitities.item import Event
from app.ports.repositories.event_repository import EventRepository
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyProductNameError,
    InvalidProductPriceError,
    NegativeStockError,
    NonPositiveWeightError,
)


class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def __call__(self, event: Event) -> None:
        if event.price <= 0:
            raise InvalidProductPriceError()

        if not event.name:
            raise EmptyProductNameError()

        if not event.organizer:
            raise EmptyProductNameError()

        await self.event_repository.add(event)
