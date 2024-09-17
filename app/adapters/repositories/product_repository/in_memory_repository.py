from itertools import product
from typing import Any, List
from uuid import UUID

from app.domain.enitities.item import Product
from app.ports.repositories.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    products: List[Product] = []

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
