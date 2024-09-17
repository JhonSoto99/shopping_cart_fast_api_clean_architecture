from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.event_repository.mongodb_repository import (
    MongoEventRepository,
)
from app.adapters.repositories.product_repository.mongodb_repository import (
    MongoProductRepository,
)
from app.adapters.repositories.shopping_cart_repository.in_memory_repository import (
    InMemoryShoppingCartRepository,
)
from app.domain.enitities.item import Product
from app.ports.repositories.cart_repository import ShoppingCartRepository
from app.ports.repositories.event_repository import EventRepository
from app.ports.repositories.product_repository import ProductRepository
from app.use_cases.add_item_to_cart_case_use import CreateCartUseCase
from app.use_cases.create_event_use_case import CreateEventUseCase
from app.use_cases.create_product_use_case import CreateProductUseCase
from app.use_cases.get_all_events_use_case import GetAllEventsUseCase
from app.use_cases.get_all_products_use_case import GetAllProductsUseCase
from app.use_cases.get_shopping_cart_case_use import GetShoppingCartUseCase


@lru_cache
def get_mongo_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient("mongodb://localhost:27017")


def get_product_repository(
    mongo_client: Annotated[AsyncIOMotorClient, Depends(get_mongo_client)],
) -> ProductRepository:
    return MongoProductRepository(mongo_client)


def get_created_product_use_case(
    product_repository: Annotated[
        ProductRepository, Depends(get_product_repository)
    ],
) -> CreateProductUseCase:
    return CreateProductUseCase(product_repository)


def get_all_products_use_case(
    product_repository: Annotated[
        ProductRepository, Depends(get_product_repository)
    ],
) -> GetAllProductsUseCase:
    return GetAllProductsUseCase(product_repository)


def get_event_repository(
    mongo_client: Annotated[AsyncIOMotorClient, Depends(get_mongo_client)],
) -> EventRepository:
    return MongoEventRepository(mongo_client)


def get_created_event_use_case(
    event_repository: Annotated[EventRepository, Depends(get_event_repository)],
) -> CreateEventUseCase:
    return CreateEventUseCase(event_repository)


def get_all_events_use_case(
    event_repository: Annotated[EventRepository, Depends(get_event_repository)],
) -> GetAllEventsUseCase:
    return GetAllEventsUseCase(event_repository)


def get_shopping_cart_repository() -> InMemoryShoppingCartRepository:
    # Inicializar o devolver un repositorio en memoria
    return InMemoryShoppingCartRepository()


def get_created_item_to_cart_use_case(
    shopping_cart_repository: Annotated[
        ShoppingCartRepository, Depends(get_shopping_cart_repository)
    ],
    event_repository: Annotated[EventRepository, Depends(get_event_repository)],
    product_repository: Annotated[
        ProductRepository, Depends(get_product_repository)
    ],
) -> CreateCartUseCase:
    return CreateCartUseCase(
        shopping_cart_repository, event_repository, product_repository
    )


def get_shopping_cart_use_case(
    shopping_cart_repository: Annotated[
        InMemoryShoppingCartRepository, Depends(get_shopping_cart_repository)
    ],
) -> GetShoppingCartUseCase:
    return GetShoppingCartUseCase(shopping_cart_repository)
