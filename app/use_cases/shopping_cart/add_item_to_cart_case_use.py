from uuid import UUID

from app.domain.enitities.cart import CartItem
from app.ports.repositories.cart_repository import ShoppingCartRepository
from app.ports.repositories.event_repository import EventRepository
from app.ports.repositories.product_repository import ProductRepository
from app.tests.integration.repositories.mongodb_event_repository_test import (
    event_repository,
)
from app.use_cases.exceptions import InsufficientStockError, ItemNotFoundError


class CreateCartUseCase:
    def __init__(
        self,
        shopping_cart_repository: ShoppingCartRepository,
        event_repository: EventRepository,
        product_repository: ProductRepository,
    ):
        self.shopping_cart_repository = shopping_cart_repository
        self.event_repository = event_repository
        self.product_repository = product_repository

    async def __call__(
        self, item_id: UUID, item_type: str, quantity: int
    ) -> None:
        item = None
        if item_type == "product":
            item = await self.product_repository.get(id=item_id)

        elif item_type == "event":
            item = await self.event_repository.get(id=item_id)

        if item is None:
            raise ItemNotFoundError()

        if item.stock < quantity:
            raise InsufficientStockError()

        new_stock = item.stock - quantity

        if item_type == "product":
            await self.product_repository.update_stock(item_id, new_stock)

        elif item_type == "event":
            await self.event_repository.update_stock(item_id, new_stock)

        # Verifica si el ítem ya existe en el carrito
        existing_item = await self.shopping_cart_repository.get_item(
            item_id, item_type
        )

        if existing_item:
            # Si el ítem ya existe en el carrito, suma la cantidad
            new_quantity = existing_item.quantity + quantity
            await self.shopping_cart_repository.update_item_quantity(
                item_id, item_type, new_quantity
            )
        else:
            await self.shopping_cart_repository.add_item_to_cart(item, quantity)
