from uuid import UUID, uuid4

from black import datetime

from app.domain.enitities.item import Event, Product


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


def create_event(
    event_id: UUID | None = None,
    price: int = 2000,
    stock: int = 50,
    name: str = "Mentoría Desarrollo Personal",
    thumbnail: str = "image.jpg",
    description: str = "Eleva tu mente.",
    organizer: str = "John Soto",
    event_date: datetime | None = None,
    venue: str = "Cali, Colombia",
) -> Event:
    return Event(
        id=event_id if event_id else uuid4(),
        price=price,
        stock=stock,
        name=name,
        thumbnail=thumbnail,
        description=description,
        organizer=organizer,
        event_date=event_date,
        venue=venue,
    )
