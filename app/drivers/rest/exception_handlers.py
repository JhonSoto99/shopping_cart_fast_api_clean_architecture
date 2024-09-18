from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.adapters.exceptions import ExternalError
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyEventDateError,
    EmptyEventOrganizerError,
    EmptyProductDescriptionError,
    EmptyProductNameError,
    EmptyProductThumbnailError,
    EmptyVenueError,
    InsufficientStockError,
    InvalidProductPriceError,
    ItemNotFoundError,
    NegativeStockError,
    NonPositiveWeightError,
)


def exception_container(app: FastAPI) -> None:

    @app.exception_handler(InvalidProductPriceError)
    async def invalid_product_price_exception_handler(
        request: Request, exc: InvalidProductPriceError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyProductNameError)
    async def empty_product_name_exception_handler(
        request: Request, exc: EmptyProductNameError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyProductThumbnailError)
    async def empty_product_thumbnail_exception_handler(
        request: Request, exc: EmptyProductThumbnailError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyProductDescriptionError)
    async def empty_product_description_exception_handler(
        request: Request, exc: EmptyProductDescriptionError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(NegativeStockError)
    async def negative_stock_error_exception_handler(
        request: Request, exc: NegativeStockError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(NonPositiveWeightError)
    async def non_positive_weight_exception_handler(
        request: Request, exc: NonPositiveWeightError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyBrandError)
    async def empty_brand_error_exception_handler(
        request: Request, exc: EmptyBrandError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(ItemNotFoundError)
    async def item_not_found_error_exception_handler(
        request: Request, exc: ItemNotFoundError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(InsufficientStockError)
    async def insufficient_stock_error_exception_handler(
        request: Request, exc: InsufficientStockError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(ExternalError)
    async def external_exception_handler(
        request: Request, exc: ExternalError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyEventOrganizerError)
    async def empty_event_organizer_error_exception_handler(
        request: Request, exc: EmptyEventOrganizerError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyEventDateError)
    async def empty_event_date_error_exception_handler(
        request: Request, exc: EmptyEventDateError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )

    @app.exception_handler(EmptyVenueError)
    async def empty_event_venue_error_exception_handler(
        request: Request, exc: EmptyVenueError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"message": str(exc)},
        )
