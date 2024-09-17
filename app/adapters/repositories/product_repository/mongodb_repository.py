from abc import ABC
from typing import Any, List
from typing import Optional
from uuid import UUID

from bson import Binary
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError

from app.adapters.exceptions import DatabaseError
from app.domain.enitities.item import Product
from app.ports.repositories.product_repository import ProductRepository


class MongoProductRepository(ProductRepository):
    def __init__(self, client: AsyncIOMotorClient):
        self.collection = client.products.product

    async def get(self, **filters: Any) -> Product | None:
        filters = self.__get_filters(filters)
        try:
            document = await self.collection.find_one(filters)
            return self.__to_product_entity(document) if document else None
        except Exception as e:
            raise DatabaseError(e)

    async def get_by_id(self, product_id: UUID) -> Optional[Product]:
        try:
            document = self.collection.find_one({"_id": Binary.from_uuid(product_id)})
            if document:
                return self.__to_product_entity(document)  # Convertir el documento a entidad de producto
            return None
        except PyMongoError as e:
            raise DatabaseError(e)
        except Exception as e:
            raise ValueError(f"Invalid ObjectId: {product_id}")

    async def get_all(self, **filters: Any) -> List[Product]:
        filters = self.__get_filters(filters)
        try:
            cursor = self.collection.find(filters)
            documents = await cursor.to_list(
                length=None
            )  # Convertir el cursor a una lista
            return [
                self.__to_product_entity(document) for document in documents
            ]
        except PyMongoError as e:
            raise DatabaseError(e)

    async def add(self, product: Product) -> bool:
        try:
            product_doc = self.__product_to_doc(product)
            result = await self.collection.insert_one(product_doc)
            return result.acknowledged
        except Exception as e:
            raise DatabaseError(e)

    @staticmethod
    def __get_filters(filters_args: dict[str, Any]) -> dict[str, Any]:
        filters = {}
        if f := filters_args.get("id"):
            filters["_id"] = Binary.from_uuid(f)
        return filters

    def __product_to_doc(self, product: Product) -> dict[str, Any]:
        return {
            "_id": Binary.from_uuid(product.id),
            "price": product.price,
            "name": product.name,
            "thumbnail": product.thumbnail,
            "description": product.description,
            "stock": product.stock,
            "weight": product.weight,
            "brand": product.brand,
        }

    def __to_product_entity(self, obj: dict[str, Any]) -> Product:
        return Product(
            id=UUID(bytes=obj["_id"]),
            price=obj["price"],
            name=obj["name"],
            thumbnail=obj["thumbnail"],
            description=obj["description"],
            stock=obj["stock"],
            weight=obj["weight"],
            brand=obj["brand"],
        )
