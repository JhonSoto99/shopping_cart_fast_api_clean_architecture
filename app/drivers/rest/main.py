from fastapi import FastAPI

from app.drivers.rest.constants.values import API_V1_PREFIX
from app.drivers.rest.exception_handlers import exception_container
from app.drivers.rest.routers import event, product, shopping_cart

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

origins = ["*"]

app.title = "App Backend Samy - Carrito de Compras."
app.version = "0.0.1"


app.include_router(product.router, prefix=API_V1_PREFIX)
app.include_router(event.router, prefix=API_V1_PREFIX)
app.include_router(shopping_cart.router, prefix=API_V1_PREFIX)

exception_container(app)
