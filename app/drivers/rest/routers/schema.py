from typing import List
from uuid import UUID

from black import datetime
from pydantic import BaseModel

from app.domain.enitities.cart import CartItem
from app.domain.enitities.item import Event, Product


class ProductInput(BaseModel):
    product_id: UUID
    price: int
    name: str
    thumbnail: str
    description: str
    stock: int
    weight: float
    brand: str

    def to_entity(self) -> Product:
        return Product(
            id=self.product_id,
            price=self.price,
            name=self.name,
            thumbnail=self.thumbnail,
            description=self.description,
            stock=self.stock,
            weight=self.weight,
            brand=self.brand,
        )


class ProductOutput(BaseModel):
    id: UUID
    price: int
    name: str
    thumbnail: str
    description: str
    stock: int
    weight: float
    brand: str

    class Config:
        orm_mode = True


class EventOutput(BaseModel):
    id: UUID
    price: int
    name: str
    thumbnail: str
    description: str
    organizer: str
    event_date: datetime
    venue: str

    class Config:
        orm_mode = True


class EventInput(BaseModel):
    event_id: UUID
    price: int
    name: str
    thumbnail: str
    description: str
    organizer: str
    event_date: datetime
    venue: str

    def to_entity(self) -> Event:
        return Event(
            id=self.event_id,
            price=self.price,
            name=self.name,
            thumbnail=self.thumbnail,
            description=self.description,
            organizer=self.organizer,
            event_date=self.event_date,
            venue=self.venue,
        )


class CartItemOutput(BaseModel):
    item_id: UUID
    name: str
    price: int
    quantity: int
    item_type: str  # Puede ser 'Product' o 'Event'


class ShoppingCartOutput(BaseModel):
    items: List[CartItemOutput]

    class Config:
        orm_mode = True
