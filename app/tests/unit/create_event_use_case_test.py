from datetime import datetime

import pytest

from app.tests.utils import create_event
from app.use_cases.event.create_event_use_case import CreateEventUseCase
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


@pytest.mark.asyncio
async def test_add_valid_event(create_event_use_case: CreateEventUseCase):
    product = create_event(event_date=datetime.now())
    await create_event_use_case(product)


@pytest.mark.asyncio
async def test_add_invalid_event(
    create_event_use_case: CreateEventUseCase,
):
    invalid_event = create_event(
        price=-100,
        stock=-7,
        name="",
        thumbnail="",
        description="",
        organizer="",
        event_date=None,
        venue="",
    )

    with pytest.raises(InvalidProductPriceError):
        await create_event_use_case(invalid_event)

    invalid_event.price = 100
    with pytest.raises(EmptyProductNameError):
        await create_event_use_case(invalid_event)

    invalid_event.name = "Evento válido"
    with pytest.raises(NegativeStockError):
        await create_event_use_case(invalid_event)

    invalid_event.stock = 100
    with pytest.raises(EmptyProductThumbnailError):
        await create_event_use_case(invalid_event)

    invalid_event.thumbnail = "https://example.com/thumbnail.png"
    with pytest.raises(EmptyProductDescriptionError):
        await create_event_use_case(invalid_event)

    invalid_event.description = "Descripción del evento"
    with pytest.raises(EmptyEventOrganizerError):
        await create_event_use_case(invalid_event)

    invalid_event.organizer = "Organizador del evento"
    with pytest.raises(EmptyEventDateError):
        await create_event_use_case(invalid_event)

    invalid_event.event_date = datetime.now()
    with pytest.raises(EmptyVenueError):
        await create_event_use_case(invalid_event)

    invalid_event.venue = "Lugar del evento"
    await create_event_use_case(invalid_event)
