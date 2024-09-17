from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from app.domain.enitities.cart import CartItem, ShoppingCart
from app.drivers.rest.routers.schema import ShoppingCartOutput


class ShoppingCartRepository(ABC):
    @abstractmethod
    async def get(self) -> ShoppingCart:
        pass

    @abstractmethod
    async def add_item_to_cart(
        self, cart_item: CartItem, quantity: int
    ) -> None:
        pass

    @abstractmethod
    async def get_item(
        self, item_id: UUID, item_type: str
    ) -> Optional[CartItem]:
        pass

    @abstractmethod
    async def update_item_quantity(
        self, item_id: UUID, item_type: str, new_quantity: int
    ) -> None:
        pass

    @abstractmethod
    async def remove_item_from_cart(
        self, item_id: UUID, item_type: str
    ) -> bool:
        pass
