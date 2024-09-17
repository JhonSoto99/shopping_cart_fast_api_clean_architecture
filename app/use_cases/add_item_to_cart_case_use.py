from app.domain.enitities.cart import CartItem
from app.ports.repositories.cart_repository import ShoppingCartRepository
from app.use_cases.exceptions import (
    EmptyBrandError,
    EmptyProductNameError,
    InvalidProductPriceError,
    NegativeStockError,
    NonPositiveWeightError,
)


class CreateCartUseCase:
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self.shopping_cart_repository = shopping_cart_repository

    async def __call__(self, cart_item: CartItem) -> None:
        await self.shopping_cart_repository.add_item_to_cart(cart_item)
