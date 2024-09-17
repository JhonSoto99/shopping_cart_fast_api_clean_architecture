import asyncio
from uuid import uuid4

import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.product_repository.mongodb_repository import (
    MongoProductRepository,
)
from app.tests.utils import create_product


@pytest.fixture
def product_repository(client: AsyncIOMotorClient):
    repo = MongoProductRepository(client)
    yield repo
    repo.collection.drop()


@pytest.mark.asyncio
async def test_add_product_success(product_repository: MongoProductRepository):
    product = create_product()  # Crea un producto con datos válidos
    result = await product_repository.add(product)  # Añade el producto
    assert result is True  # Verifica que el producto se añadió correctamente
