from datetime import datetime

import pytest

from app.tests.utils import create_event
from app.use_cases.create_event_use_case import CreateEventUseCase
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyProductNameError,
    InvalidProductPriceError,
    NegativeStockError,
    NonPositiveWeightError,
)


@pytest.mark.asyncio
async def test_add_valid_event(create_event_use_case: CreateEventUseCase):
    product = create_event()
    await create_event_use_case(product)


@pytest.mark.asyncio
async def test_add_invalid_event(
    create_event_use_case: CreateEventUseCase,
):
    invalid_event = create_event(
        price=-100,
        name="",
        thumbnail="",
        description="",
        organizer="",
        event_date=datetime.now(),
        venue="",
    )

    with pytest.raises(InvalidProductPriceError):
        await create_event_use_case(invalid_event)

    # invalid_event.price = 100
    # with pytest.raises(EmptyProductNameError):
    #    await create_event_use_case(invalid_event)

    # invalid_event.name = "Evento válido"
    # with pytest.raises(NegativeStockError):
    #    await create_event_use_case(invalid_event)
