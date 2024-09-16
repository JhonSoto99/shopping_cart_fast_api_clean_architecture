from uuid import UUID, uuid4

from app.domain.enitities.item import Product


def create_product(
    product_id: UUID | None = None,
    price: int = 2000,
    name: str = "Vaso",
    thumbnail: str = "image.jpg",
    description: str = "Vaso de colores.",
    stock: int = 50,
    weight: float = 2.5,
    brand: str = "Corona",
) -> Product:
    return Product(
        id=product_id if product_id else uuid4(),
        price=price,
        name=name,
        thumbnail=thumbnail,
        description=description,
        stock=stock,
        weight=weight,
        brand=brand,
    )
