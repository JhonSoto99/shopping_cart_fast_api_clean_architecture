from app.domain.enitities.cart import ShoppingCart
from app.ports.repositories.cart_repository import ShoppingCartRepository


class GetShoppingCartUseCase:
    def __init__(self, shopping_cart_repository: ShoppingCartRepository):
        self.shopping_cart_repository = shopping_cart_repository

    async def __call__(self) -> ShoppingCart:
        return await self.shopping_cart_repository.get()
