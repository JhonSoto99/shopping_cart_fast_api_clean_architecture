from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class ItemBase:
    price: int
    name: str
    thumbnail: str
    description: str
    stock: int
    id: UUID = field(default_factory=uuid4)


@dataclass(kw_only=True)
class Product(ItemBase):
    weight: float
    brand: str


@dataclass(kw_only=True)
class Event(ItemBase):
    organizer: str
    event_date: datetime
    venue: str
