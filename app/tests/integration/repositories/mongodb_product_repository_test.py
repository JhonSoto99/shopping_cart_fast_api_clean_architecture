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
    product = create_product()
    result = await product_repository.add(product)
    assert result is True
