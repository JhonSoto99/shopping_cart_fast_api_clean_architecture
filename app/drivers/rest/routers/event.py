from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from app.drivers.rest.constants.values import STATUS_CODE_MESSAGES
from app.drivers.rest.dependencies import (
    get_all_events_use_case,
    get_created_event_use_case,
)
from app.drivers.rest.routers.schema import EventCreate, EventOutput
from app.use_cases.event.create_event_use_case import CreateEventUseCase
from app.use_cases.event.get_all_events_use_case import GetAllEventsUseCase

router = APIRouter(prefix="/events")


@router.post(
    "/create",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Eventos"],
    responses={
        204: {
            "description": STATUS_CODE_MESSAGES[204],
            "content": {"application/json": {"example": {}}},
        },
        422: {
            "description": STATUS_CODE_MESSAGES[422],
            "content": {
                "application/json": {
                    "example": {
                        "message": "The product price must be greater than 0."
                    }
                }
            },
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def create_event(
    data: EventCreate,
    use_case: Annotated[
        CreateEventUseCase, Depends(get_created_event_use_case)
    ],
) -> None:
    """
    Recurso para crear un evento.

    **Request Parameters:**
    - price (int): Precio del evento.
    - name (str): Nombre del evento.
    - stock (int): Stock del evento.
    - thumbnail (str): Foto del evento.
    - description (str): Descripción del evento.
    - organizer (str): Organizador del evento.
    - event_date (date): Fecha del evento.
    - venue (str): Lugar del evento.

    **Responses:**
    - **204**: Se creó exitosamente.
    - **422**: Datos enviados inválidos.
    - **500**: Error interno del servidor.

    **Example Successful Not Content (204):**
    ```json
    {}
    ```

    **Example Validation Error Response (422):**
    ```json
    {
      "message": "The end date must be greater than the start date."
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    await use_case(data.to_entity())


@router.get(
    "/",
    response_model=List[EventOutput],
    status_code=status.HTTP_200_OK,
    tags=["Eventos"],
    responses={
        200: {
            "description": STATUS_CODE_MESSAGES[200],
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": "bdbfed59-a07e-46e3-83fc-83de43819c58",
                            "price": 11110,
                            "name": "string",
                            "stock": 0,
                            "thumbnail": "string",
                            "description": "string",
                            "organizer": "string",
                            "event_date": "2024-09-18T04:03:09.562000",
                            "venue": "string",
                        }
                    ]
                }
            },
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def get_events(
    use_case: Annotated[GetAllEventsUseCase, Depends(get_all_events_use_case)],
) -> List[EventOutput]:
    """
    Recurso para obtener un evento.

    **Request Parameters:**

    **Responses:**
    - **200**: Se obtuvo exitosamente.
    - **500**: Error interno del servidor.

    **Example Successful (200):**
    ```json
    [
      {
        "id": "20f83a84-24df-46d4-9290-3f6677735cd3",
        "price": 3232330,
        "name": "Evento1",
        "thumbnail": "string",
        "description": "Evento 1",
        "stock": 30
        "event_date": "2023-01-01"
        "avenue": "Cali, Colombia"
      }
    ]
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    events = await use_case()
    return events
