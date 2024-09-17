import pytest
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.event_repository.mongodb_repository import (
    MongoEventRepository,
)
from app.tests.utils import create_event


@pytest.fixture
def event_repository(client: AsyncIOMotorClient):
    repo = MongoEventRepository(client)
    yield repo
    repo.collection.drop()


@pytest.mark.asyncio
async def test_add_event_success(event_repository: MongoEventRepository):
    event = create_event()
    result = await event_repository.add(event)
    assert result is True
