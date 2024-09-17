from uuid import UUID

from app.domain.enitities.cart import CartItem
from app.ports.repositories.cart_repository import ShoppingCartRepository
from app.ports.repositories.event_repository import EventRepository
from app.ports.repositories.product_repository import ProductRepository
from app.tests.integration.repositories.mongodb_event_repository_test import event_repository


class CreateCartUseCase:
    def __init__(self,
                 shopping_cart_repository: ShoppingCartRepository,
                 event_repository: EventRepository,
                 product_repository: ProductRepository,
                 ):
        self.shopping_cart_repository = shopping_cart_repository
        self.event_repository = event_repository
        self.product_repository = product_repository

    async def __call__(self, item_id: UUID, item_type: str, quantity: int) -> None:
        item = None
        if item_type == "product":
            item = await self.product_repository.get(id=item_id)

        elif item_type == "event":
            item = await self.event_repository.get(id=item_id)

        if item is None:
            raise ValueError("Item not found")

        await self.shopping_cart_repository.add_item_to_cart(item, quantity)
