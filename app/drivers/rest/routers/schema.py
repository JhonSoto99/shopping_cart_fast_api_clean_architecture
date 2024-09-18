from typing import List, Literal
from uuid import UUID, uuid4

from black import datetime
from pydantic import BaseModel, Field

from app.domain.enitities.item import Event, Product


class ProductCreate(BaseModel):
    price: int
    name: str
    thumbnail: str
    description: str
    stock: int
    weight: float
    brand: str

    def to_entity(self) -> Product:
        return Product(
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
    stock: int
    thumbnail: str
    description: str
    organizer: str
    event_date: datetime
    venue: str

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    price: int
    name: str
    stock: int
    thumbnail: str
    description: str
    organizer: str
    event_date: datetime
    venue: str

    def to_entity(self) -> Event:
        return Event(
            price=self.price,
            stock=self.stock,
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


class AddItemToCartRequest(BaseModel):
    item_id: UUID
    quantity: int = Field(
        ..., gt=0, description="Quantity must be greater than 0"
    )
    item_type: Literal["product", "event"]


class DeleteItemFromCartRequest(BaseModel):
    item_id: UUID
    item_type: Literal["product", "event"]


class UpdateItemQuantityRequest(BaseModel):
    item_id: UUID
    item_type: Literal["product", "event"]
    new_quantity: int
