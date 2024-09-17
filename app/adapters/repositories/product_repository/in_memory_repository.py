from itertools import product
from typing import Any, List
from uuid import UUID

from app.domain.enitities.item import Product
from app.ports.repositories.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    products: List[Product] = []

    async def update_stock(self, product_id: UUID, new_stock: int):
        for product in self.products:
            if product.id == product_id:
                product.stock = new_stock
                return

    def clear(self):
        self.products = []

    async def get(self, **filters: Any) -> Product | None:
        for product in self.products:
            if (f := filters.get("id")) and f == product.id:
                return product
        return None

    async def get_all(self) -> List[Product]:
        return self.products

    async def add(self, product: Product) -> bool:
        self.products.append(product)
        return True
