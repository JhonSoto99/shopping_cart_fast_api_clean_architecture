from typing import Any, List
from uuid import UUID

from bson import Binary
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import PyMongoError

from app.adapters.exceptions import DatabaseError
from app.domain.enitities.item import Event
from app.ports.repositories.event_repository import EventRepository
from app.use_cases.exceptions import ItemNotFoundError


class MongoEventRepository(EventRepository):
    def __init__(self, client: AsyncIOMotorClient):
        self.collection = client.events.event

    async def update_stock(self, event_id: UUID, new_stock: int):
        try:
            result = await self.collection.update_one(
                {"_id": Binary.from_uuid(event_id)},
                {"$set": {"stock": new_stock}},
            )
            if result.matched_count == 0:
                raise ItemNotFoundError()
        except PyMongoError as e:
            raise DatabaseError(e)

    async def get(self, **filters: Any) -> Event | None:
        filters = self.__get_filters(filters)
        try:
            document = await self.collection.find_one(filters)
            return self.__to_event_entity(document) if document else None
        except Exception as e:
            raise DatabaseError(e)

    async def get_all(self, **filters: Any) -> List[Event]:
        filters = self.__get_filters(filters)
        try:
            cursor = self.collection.find(filters)
            documents = await cursor.to_list(
                length=None
            )  # Convertir el cursor a una lista
            return [self.__to_event_entity(document) for document in documents]
        except PyMongoError as e:
            raise DatabaseError(e)

    async def add(self, event: Event) -> bool:
        try:
            event_doc = self.__event_to_doc(event)
            result = await self.collection.insert_one(event_doc)
            return result.acknowledged
        except Exception as e:
            raise DatabaseError(e)

    @staticmethod
    def __get_filters(filters_args: dict[str, Any]) -> dict[str, Any]:
        filters = {}
        if f := filters_args.get("id"):
            filters["_id"] = Binary.from_uuid(f)
        return filters

    def __event_to_doc(self, event: Event) -> dict[str, Any]:
        return {
            "_id": Binary.from_uuid(event.id),
            "price": event.price,
            "stock": event.stock,
            "name": event.name,
            "thumbnail": event.thumbnail,
            "description": event.description,
            "organizer": event.organizer,
            "event_date": event.event_date,
            "venue": event.venue,
        }

    def __to_event_entity(self, obj: dict[str, Any]) -> Event:
        return Event(
            id=UUID(bytes=obj["_id"]),
            price=obj["price"],
            stock=obj["stock"],
            name=obj["name"],
            thumbnail=obj["thumbnail"],
            description=obj["description"],
            organizer=obj["organizer"],
            event_date=obj["event_date"],
            venue=obj["venue"],
        )
