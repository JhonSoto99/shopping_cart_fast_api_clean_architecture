from typing import Any, List

from app.domain.enitities.item import Product
from app.ports.repositories.product_repository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    products: List[Product] = []

    async def get(self, **filters: Any) -> Product | None:
        for product in self.products:
            if (f := filters.get("id")) and f == product.id:
                return product
        return None

    async def add(self, product: Product) -> bool:
        self.products.append(product)
        return True
