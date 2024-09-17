from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.drivers.rest.exception_handlers import exception_container
from app.drivers.rest.routers import product

app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

origins = ["*"]

app.title = "App Backend Samy - Carrito de Compras."
app.version = "0.0.1"


app.include_router(product.router)

exception_container(app)
