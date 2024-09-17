from app.domain.enitities.cart import CartItem, ShoppingCart
from app.drivers.rest.routers.schema import ShoppingCartOutput
from app.ports.repositories.cart_repository import ShoppingCartRepository


class InMemoryShoppingCartRepository(ShoppingCartRepository):
    shopping_cart = ShoppingCart()

    def clear(self):
        self.shopping_cart: ShoppingCart

    async def get(self) -> ShoppingCart:
        return self.shopping_cart

    async def add_item_to_cart(self, cart_item: CartItem, quantity: int) -> bool:
        cart_item.quantity = quantity
        self.shopping_cart.items.append(cart_item)
        return True
