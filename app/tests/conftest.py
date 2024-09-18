import asyncio

import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.event_repository.in_memory_repository import (
    InMemoryEventRepository,
)
from app.adapters.repositories.product_repository.in_memory_repository import (
    InMemoryProductRepository,
)
from app.ports.repositories.event_repository import EventRepository
from app.ports.repositories.product_repository import ProductRepository
from app.use_cases.event.create_event_use_case import CreateEventUseCase
from app.use_cases.products.create_product_use_case import CreateProductUseCase


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def client():
    return AsyncIOMotorClient("mongodb://mongo-events:27017")


@pytest.fixture
def products_repository() -> ProductRepository:
    repo = InMemoryProductRepository()
    repo.clear()
    return repo


@pytest.fixture
def create_product_use_case(
    products_repository: ProductRepository,
) -> CreateProductUseCase:
    return CreateProductUseCase(products_repository)


@pytest.fixture
def events_repository() -> EventRepository:
    repo = InMemoryEventRepository()
    repo.clear()
    return repo


@pytest.fixture
def create_event_use_case(
    events_repository: EventRepository,
) -> CreateEventUseCase:
    return CreateEventUseCase(events_repository)
