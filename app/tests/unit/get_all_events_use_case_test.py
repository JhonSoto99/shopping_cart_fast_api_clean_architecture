import pytest

from app.ports.repositories.event_repository import EventRepository
from app.tests.utils import create_event
from app.use_cases.create_event_use_case import CreateEventUseCase
from app.use_cases.get_all_events_use_case import GetAllEventsUseCase


@pytest.fixture
def get_all_events_use_case(
    events_repository: EventRepository,
) -> GetAllEventsUseCase:
    return GetAllEventsUseCase(events_repository)


@pytest.mark.asyncio
async def test_get_all_events_success(
    get_all_events_use_case: GetAllEventsUseCase,
    create_event_use_case: CreateEventUseCase,
):
    event1 = create_event()
    event2 = create_event()
    await create_event_use_case(event1)
    await create_event_use_case(event2)
    events = await get_all_events_use_case()
    assert len(events) == 2


@pytest.mark.asyncio
async def test_get_all_events_empty(
    get_all_events_use_case: GetAllEventsUseCase,
):
    events = await get_all_events_use_case()
    assert events == []
