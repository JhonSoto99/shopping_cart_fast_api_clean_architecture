import time

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.models import Response

from app.drivers.rest.exception_handlers import exception_container
from app.drivers.rest.routers import product

from .logger import logger

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

origins = ["*"]

app.title = "App Backend Samy - Carrito de Compras."
app.version = "0.0.1"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next) -> Response:
    """
    Middleware para registrar la información de cada solicitud HTTP
    y el tiempo de procesamiento.

    Este middleware registra el método y la URL de la solicitud,
    y también el tiempo que tarda en procesar la solicitud.
    Al finalizar el procesamiento, también registra el código
    de estado de la respuesta y el tiempo total transcurrido.

    Args:
        request (Request): El objeto de solicitud de FastAPI,
            que contiene detalles sobre la solicitud HTTP entrante.
        call_next (Callable): La función que se llama para pasar
            la solicitud al siguiente middleware o ruta en la
            cadena de procesamiento.

    Returns:
        Response: La respuesta HTTP generada por el siguiente
            middleware o ruta en la cadena de procesamiento.
    """
    logger.info("Request: %s %s.", request.method, request.url)

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(
        "Completed in %s.4f sec - Status code: %s.",
        process_time,
        response.status_code,
    )

    return response


app.include_router(product.router)

exception_container(app)
