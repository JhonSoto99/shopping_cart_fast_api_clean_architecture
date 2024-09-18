from dataclasses import dataclass
from typing import List, Literal, Union
from uuid import UUID

from app.domain.enitities.item import Event, Product


@dataclass(kw_only=True)
class CartItem:
    id: UUID
    name: str
    item: Union[Product, Event]
    quantity: int
    item_type: Literal["product", "event"]
    price: int
    stock: int


@dataclass(kw_only=True)
class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []
