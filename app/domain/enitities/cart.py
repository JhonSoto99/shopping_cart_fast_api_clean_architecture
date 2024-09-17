from dataclasses import dataclass, field
from typing import List, Union
from uuid import UUID, uuid4

from app.domain.enitities.item import Event, Product


@dataclass(kw_only=True)
class CartItem:
    item: Union[Product, Event]  # Puede ser un producto o un evento
    quantity: int


@dataclass(kw_only=True)
class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []

    def add_item(self, item: Union[Product, Event], quantity: int = 1):
        # Verifica si el item ya está en el carrito
        cart_item = next((i for i in self.items if i.item.id == item.id), None)

        # Si ya existe en el carrito, aumenta la cantidad
        if cart_item:
            if (
                isinstance(item, Product)
                and cart_item.quantity + quantity > item.stock
            ):
                raise ValueError(
                    f"No hay suficiente stock para {item.name}. Stock disponible: {item.stock}"
                )
            cart_item.quantity += quantity
        else:
            # Verifica que haya suficiente stock si es un producto
            if isinstance(item, Product) and quantity > item.stock:
                raise ValueError(
                    f"No hay suficiente stock para {item.name}. Stock disponible: {item.stock}"
                )
            # Agrega el item al carrito
            self.items.append(CartItem(item=item, quantity=quantity))

    def remove_item(self, item_id: UUID, quantity: int = 1):
        # Busca el item en el carrito
        cart_item = next((i for i in self.items if i.item.id == item_id), None)

        if cart_item:
            # Si la cantidad llega a 0 o menos, elimina el item
            if cart_item.quantity <= quantity:
                self.items.remove(cart_item)
            else:
                cart_item.quantity -= quantity

    def get_total(self) -> int:
        # Calcula el total del carrito
        return sum(item.item.price * item.quantity for item in self.items)

    def get_cart_details(self):
        # Obtén un resumen de los items en el carrito
        return [
            (item.item.name, item.quantity, item.item.price * item.quantity)
            for item in self.items
        ]
