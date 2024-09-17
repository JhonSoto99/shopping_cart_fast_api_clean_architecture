from abc import ABC, abstractmethod

from app.domain.enitities.cart import CartItem, ShoppingCart
from app.drivers.rest.routers.schema import ShoppingCartOutput


class ShoppingCartRepository(ABC):
    @abstractmethod
    async def get(self) -> ShoppingCart:
        pass

    @abstractmethod
    async def add_item_to_cart(self, cart_item: CartItem, quantity: int) -> bool:
        pass
