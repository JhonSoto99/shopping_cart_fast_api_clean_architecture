import asyncio
from uuid import uuid4

import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.product_repository.mongodb_repository import (
    MongoProductRepository,
)
from app.tests.utils import create_product


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def client():
    return AsyncIOMotorClient("mongodb://localhost:27017")


@pytest.fixture
def product_repository(client: AsyncIOMotorClient):
    repo = MongoProductRepository(client)
    yield repo
    repo.collection.drop()


@pytest.mark.asyncio
async def test_get_by_id_success(product_repository: MongoProductRepository):
    product = create_product()  # Crea un producto con datos válidos
    await product_repository.add(product)  # Añade el producto al repositorio
    retrieved_product = await product_repository.get(
        id=product.id
    )  # Recupera el producto
    assert (
        retrieved_product == product
    )  # Verifica si el producto recuperado es igual al añadido


@pytest.mark.asyncio
async def test_get_by_id_not_found(product_repository: MongoProductRepository):
    assert (
        await product_repository.get(id=uuid4()) is None
    )  # Intenta recuperar un producto inexistente


@pytest.mark.asyncio
async def test_add_product_success(product_repository: MongoProductRepository):
    product = create_product()  # Crea un producto con datos válidos
    result = await product_repository.add(product)  # Añade el producto
    assert result is True  # Verifica que el producto se añadió correctamente
