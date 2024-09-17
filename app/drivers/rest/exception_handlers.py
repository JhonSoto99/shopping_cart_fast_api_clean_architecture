from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.adapters.exceptions import ExternalError
from app.use_cases.exceptions import (
    InvalidProductPriceError,
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

    @app.exception_handler(ExternalError)
    async def external_exception_handler(
        request: Request, exc: ExternalError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
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
