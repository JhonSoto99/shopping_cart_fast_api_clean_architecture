from typing import Optional
from uuid import UUID

from app.domain.enitities.cart import CartItem, ShoppingCart
from app.drivers.rest.routers.schema import ShoppingCartOutput
from app.ports.repositories.cart_repository import ShoppingCartRepository
from app.use_cases.exceptions import ItemNotFoundError


class InMemoryShoppingCartRepository(ShoppingCartRepository):
    shopping_cart = ShoppingCart()

    def clear(self):
        self.shopping_cart: ShoppingCart

    async def get(self) -> ShoppingCart:
        return self.shopping_cart

    async def add_item_to_cart(
        self, cart_item: CartItem, quantity: int
    ) -> bool:
        cart_item.quantity = quantity
        self.shopping_cart.items.append(cart_item)
        return True

    async def get_item(
        self, item_id: UUID, item_type: str
    ) -> Optional[CartItem]:
        return next(
            (item for item in self.shopping_cart.items if item.id == item_id),
            None,
        )

    async def update_item_quantity(
        self, item_id: UUID, item_type: str, new_quantity: int
    ) -> None:

        item = await self.get_item(item_id, item_type)

        if item:
            item.quantity = new_quantity
        else:
            raise ItemNotFoundError()
