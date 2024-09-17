from uuid import UUID

from pydantic import BaseModel

from app.domain.enitities.item import Product


class ProductInput(BaseModel):
    product_id: UUID
    price: int
    name: str
    thumbnail: str
    description: str
    stock: int
    weight: float
    brand: str

    def to_entity(self) -> Product:
        return Product(
            id=self.product_id,
            price=self.price,
            name=self.name,
            thumbnail=self.thumbnail,
            description=self.description,
            stock=self.stock,
            weight=self.weight,
            brand=self.brand,
        )


class ProductOutput(BaseModel):
    id: UUID
    price: float
    name: str
    thumbnail: str
    description: str
    stock: int
    weight: float
    brand: str

    class Config:
        orm_mode = True
