import asyncio

import pytest
from motor.motor_asyncio import AsyncIOMotorClient

# @pytest.fixture(scope="session")
# async def client():
#    client = AsyncIOMotorClient("mongodb://localhost:27017")
#    yield client
#    client.close()
