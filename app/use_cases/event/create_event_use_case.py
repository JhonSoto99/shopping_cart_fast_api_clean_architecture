from app.domain.enitities.item import Event
from app.ports.repositories.event_repository import EventRepository
from app.use_cases.exceptions import (
    EmptyEventDateError,
    EmptyEventOrganizerError,
    EmptyProductDescriptionError,
    EmptyProductNameError,
    EmptyProductThumbnailError,
    EmptyVenueError,
    InvalidProductPriceError,
    NegativeStockError,
)


class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    async def __call__(self, event: Event) -> None:
        if event.price <= 0:
            raise InvalidProductPriceError()

        if not event.name:
            raise EmptyProductNameError()

        if event.stock < 0:
            raise NegativeStockError()

        if not event.thumbnail:
            raise EmptyProductThumbnailError()

        if not event.description:
            raise EmptyProductDescriptionError()

        if not event.organizer:
            raise EmptyEventOrganizerError()

        if not event.event_date:
            raise EmptyEventDateError()

        if not event.venue:
            raise EmptyVenueError()

        await self.event_repository.add(event)
