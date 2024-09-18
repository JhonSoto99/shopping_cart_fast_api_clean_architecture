from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.domain.enitities.item import Product
from app.drivers.rest.dependencies import (
    get_create_item_to_cart_use_case,
    get_delete_item_to_cart_use_case,
    get_shopping_cart_use_case,
    get_update_item_quantity_use_case,
)
from app.drivers.rest.routers.schema import (
    AddItemToCartRequest,
    CartItemOutput,
    DeleteItemFromCartRequest,
    ShoppingCartOutput,
    UpdateItemQuantityRequest,
)
from app.use_cases.shopping_cart.add_item_to_cart_case_use import (
    CreateCartUseCase,
)
from app.use_cases.shopping_cart.delete_item_cart_case_use import (
    DeleteItemCartUseCase,
)
from app.use_cases.shopping_cart.get_shopping_cart_case_use import (
    GetShoppingCartUseCase,
)
from app.use_cases.shopping_cart.update_item_cart_case_use import (
    UpdateItemQuantityUseCase,
)

router = APIRouter(prefix="/shopping-cart")


@router.post(
    "/add-item",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Carrito de Compras"],
)
async def add_item(
    data: AddItemToCartRequest,
    use_case: Annotated[
        CreateCartUseCase, Depends(get_create_item_to_cart_use_case)
    ],
) -> None:
    await use_case(data.item_id, data.item_type, data.quantity)


@router.get("/get", status_code=status.HTTP_200_OK, tags=["Carrito de Compras"])
async def get_shopping_cart(
    use_case: Annotated[
        GetShoppingCartUseCase, Depends(get_shopping_cart_use_case)
    ],
) -> ShoppingCartOutput:
    shopping_cart = await use_case()

    items = [
        CartItemOutput(
            item=item,
            item_id=item.id,
            name=item.name,
            quantity=item.quantity,
            item_type="Product" if isinstance(item, Product) else "Event",
            price=item.price,
        )
        for item in shopping_cart.items
    ]

    return ShoppingCartOutput(items=items)


@router.patch(
    "/update-item-quantity",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Carrito de Compras"],
)
async def update_item_quantity(
    data: UpdateItemQuantityRequest,
    use_case: Annotated[
        UpdateItemQuantityUseCase, Depends(get_update_item_quantity_use_case)
    ],
) -> None:
    await use_case(data.item_id, data.item_type, data.new_quantity)


@router.delete(
    "/remove-item",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Carrito de Compras"],
)
async def remove_item(
    data: DeleteItemFromCartRequest,
    use_case: Annotated[
        DeleteItemCartUseCase, Depends(get_delete_item_to_cart_use_case)
    ],
) -> None:
    await use_case(data.item_id, data.item_type)
