from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from app.adapters.repositories.product_repository.mongodb_repository import (
    MongoProductRepository,
)
from app.ports.repositories.product_repository import ProductRepository
from app.use_cases.create_product_use_case import CreateProductUseCase


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
