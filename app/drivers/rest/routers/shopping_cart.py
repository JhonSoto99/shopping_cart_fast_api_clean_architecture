from typing import Annotated, List, Union
from uuid import UUID

from fastapi import APIRouter, Depends, status

from app.domain.enitities.cart import CartItem, ShoppingCart
from app.domain.enitities.item import Event, Product
from app.drivers.rest.dependencies import (
    get_created_item_to_cart_use_case,
    get_shopping_cart_repository,
    get_shopping_cart_use_case,
)
from app.drivers.rest.routers.schema import (
    CartItemOutput,
    ProductInput,
    ProductOutput,
    ShoppingCartOutput,
)
from app.use_cases.add_item_to_cart_case_use import CreateCartUseCase
from app.use_cases.create_product_use_case import CreateProductUseCase
from app.use_cases.get_all_products_use_case import GetAllProductsUseCase
from app.use_cases.get_shopping_cart_case_use import GetShoppingCartUseCase

router = APIRouter(prefix="/shopping-cart")


@router.post("/add-item", status_code=status.HTTP_204_NO_CONTENT)
async def add_item(
    data: CartItem,
    use_case: Annotated[
        CreateCartUseCase, Depends(get_created_item_to_cart_use_case)
    ],
) -> None:
    await use_case(data)


@router.get("/get", status_code=status.HTTP_200_OK)
async def get_shopping_cart(
    use_case: Annotated[
        GetShoppingCartUseCase, Depends(get_shopping_cart_use_case)
    ],
) -> ShoppingCartOutput:
    shopping_cart = await use_case()

    items = [
        CartItemOutput(
            item_id=item.item.id,
            name=item.item.name,
            price=item.item.price,
            quantity=item.quantity,
            item_type="Product" if isinstance(item.item, Product) else "Event",
        )
        for item in shopping_cart.items
    ]

    return ShoppingCartOutput(items=items)
