from uuid import UUID

from app.ports.repositories.cart_repository import ShoppingCartRepository
from app.ports.repositories.event_repository import EventRepository
from app.ports.repositories.product_repository import ProductRepository
from app.use_cases.exceptions import InsufficientStockError, ItemNotFoundError


class UpdateItemQuantityUseCase:
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
        self, item_id: UUID, item_type: str, new_quantity: int
    ) -> None:
        existing_item = await self.shopping_cart_repository.get_item(
            item_id, item_type
        )

        if not existing_item:
            raise ItemNotFoundError()

        if new_quantity == 0:
            await self.shopping_cart_repository.remove_item_from_cart(
                item_id, item_type
            )

            if item_type == "product":
                item = await self.product_repository.get(id=item_id)
                await self.product_repository.update_stock(
                    item_id, item.stock + existing_item.quantity
                )

            elif item_type == "event":
                item = await self.event_repository.get(id=item_id)
                await self.event_repository.update_stock(
                    item_id, item.stock + existing_item.quantity
                )

        else:
            quantity_change = new_quantity - existing_item.quantity

            if quantity_change > 0:
                if item_type == "product":
                    item = await self.product_repository.get(id=item_id)
                    if item.stock < quantity_change:
                        raise InsufficientStockError()
                    await self.product_repository.update_stock(
                        item_id, item.stock - quantity_change
                    )

                elif item_type == "event":
                    item = await self.event_repository.get(id=item_id)
                    if item.stock < quantity_change:
                        raise InsufficientStockError()
                    await self.event_repository.update_stock(
                        item_id, item.stock - quantity_change
                    )

            else:
                if item_type == "product":
                    item = await self.product_repository.get(id=item_id)
                    await self.product_repository.update_stock(
                        item_id, item.stock + abs(quantity_change)
                    )

                elif item_type == "event":
                    item = await self.event_repository.get(id=item_id)
                    await self.event_repository.update_stock(
                        item_id, item.stock + abs(quantity_change)
                    )

            await self.shopping_cart_repository.update_item_quantity(
                item_id, item_type, new_quantity
            )
