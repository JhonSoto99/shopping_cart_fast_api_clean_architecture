from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from app.drivers.rest.dependencies import (
    get_all_events_use_case,
    get_created_event_use_case,
)
from app.drivers.rest.routers.schema import EventCreate, EventOutput
from app.use_cases.create_event_use_case import CreateEventUseCase
from app.use_cases.get_all_events_use_case import GetAllEventsUseCase

router = APIRouter(prefix="/events")


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def create_event(
    data: EventCreate,
    use_case: Annotated[
        CreateEventUseCase, Depends(get_created_event_use_case)
    ],
) -> None:
    await use_case(data.to_entity())


@router.get(
    "/", response_model=List[EventOutput], status_code=status.HTTP_200_OK
)
async def get_events(
    use_case: Annotated[GetAllEventsUseCase, Depends(get_all_events_use_case)],
) -> List[EventOutput]:
    events = await use_case()
    return events
