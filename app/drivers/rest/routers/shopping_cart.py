from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.domain.enitities.item import Product
from app.drivers.rest.constants.values import STATUS_CODE_MESSAGES
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
from app.services.pdf_service import generate_pdf_from_cart
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
    responses={
        204: {
            "description": STATUS_CODE_MESSAGES[204],
            "content": {"application/json": {"example": {}}},
        },
        422: {
            "description": STATUS_CODE_MESSAGES[422],
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "literal_error",
                                "loc": ["body", "item_type"],
                                "msg": "Input should be 'product' or 'event'",
                                "input": "produfct",
                                "ctx": {"expected": "'product' or 'event'"},
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def add_item(
    data: AddItemToCartRequest,
    use_case: Annotated[
        CreateCartUseCase, Depends(get_create_item_to_cart_use_case)
    ],
) -> None:
    """
    Recurso para agregar un item.

    **Request Parameters:**
    - item_id (UUID): Id del item.
    - quantity (int): Cantidad del item
    - item type (str): Tipo de item `Producto` o `Evento`

    **Responses:**
    - **204**: Se creó exitosamente.
    - **422**: Datos enviados inválidos.
    - **500**: Error interno del servidor.

    **Example Successful Not Content (204):**
    ```json
    {}
    ```

    **Example Validation Error Response (422):**
    ```json
        {
      "detail": [
        {
          "type": "literal_error",
          "loc": [
            "body",
            "item_type"
          ],
          "msg": "Input should be 'product' or 'event'",
          "input": "produfct",
          "ctx": {
            "expected": "'product' or 'event'"
          }
        }
      ]
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    await use_case(data.item_id, data.item_type, data.quantity)


@router.get(
    "/get",
    status_code=status.HTTP_200_OK,
    tags=["Carrito de Compras"],
    responses={
        200: {
            "description": STATUS_CODE_MESSAGES[200],
            "content": {
                "application/json": {
                    "example": {
                        "items": [
                            {
                                "item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                                "name": "string",
                                "price": 0,
                                "quantity": 0,
                                "item_type": "string",
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def get_shopping_cart(
    use_case: Annotated[
        GetShoppingCartUseCase, Depends(get_shopping_cart_use_case)
    ],
) -> ShoppingCartOutput:
    """
    Recurso para obtener el carrito de compras.

    **Request Parameters:**

    **Responses:**
    - **200**: Se obtuvo exitosamente.
    - **500**: Error interno del servidor.

    **Example Successful (200):**
    ```json
    {
      "items": [
        {
          "item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "name": "string",
          "price": 0,
          "quantity": 0,
          "item_type": "string"
        }
      ]
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
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
    responses={
        204: {
            "description": STATUS_CODE_MESSAGES[204],
            "content": {"application/json": {"example": {}}},
        },
        422: {
            "description": STATUS_CODE_MESSAGES[422],
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "literal_error",
                                "loc": ["body", "item_type"],
                                "msg": "Input should be 'product' or 'event'",
                                "input": "produfct",
                                "ctx": {"expected": "'product' or 'event'"},
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def update_item_quantity(
    data: UpdateItemQuantityRequest,
    use_case: Annotated[
        UpdateItemQuantityUseCase, Depends(get_update_item_quantity_use_case)
    ],
) -> None:
    """
    Recurso para actualizar la cantidad de un item
    dentro del carrito de compra.

    **Request Parameters:**
    - item_id (UUID): Id del item.
    - quantity (int): Cantidad del item
    - item type (str): Tipo de item `Producto` o `Evento`

    **Responses:**
    - **204**: Se modificó exitosamente.
    - **422**: Datos enviados inválidos.
    - **500**: Error interno del servidor.

    **Example Successful Not Content (204):**
    ```json
    {}
    ```

    **Example Validation Error Response (422):**
    ```json
        {
      "detail": [
        {
          "type": "literal_error",
          "loc": [
            "body",
            "item_type"
          ],
          "msg": "Input should be 'product' or 'event'",
          "input": "produfct",
          "ctx": {
            "expected": "'product' or 'event'"
          }
        }
      ]
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    await use_case(data.item_id, data.item_type, data.new_quantity)


@router.delete(
    "/remove-item",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Carrito de Compras"],
    responses={
        204: {
            "description": STATUS_CODE_MESSAGES[204],
            "content": {"application/json": {"example": {}}},
        },
        422: {
            "description": STATUS_CODE_MESSAGES[422],
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "type": "literal_error",
                                "loc": ["body", "item_type"],
                                "msg": "Input should be 'product' or 'event'",
                                "input": "produfct",
                                "ctx": {"expected": "'product' or 'event'"},
                            }
                        ]
                    }
                }
            },
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def remove_item(
    data: DeleteItemFromCartRequest,
    use_case: Annotated[
        DeleteItemCartUseCase, Depends(get_delete_item_to_cart_use_case)
    ],
) -> None:
    """
    Recurso para eliminar un item
    dentro del carrito de compra.

    **Request Parameters:**
    - item_id (UUID): Id del item.
    - item type (str): Tipo de item `Producto` o `Evento`

    **Responses:**
    - **204**: Se eliminó exitosamente.
    - **422**: Datos enviados inválidos.
    - **500**: Error interno del servidor.

    **Example Successful Not Content (204):**
    ```json
    {}
    ```

    **Example Validation Error Response (422):**
    ```json
        {
      "detail": [
        {
          "type": "literal_error",
          "loc": [
            "body",
            "item_type"
          ],
          "msg": "Input should be 'product' or 'event'",
          "input": "produfct",
          "ctx": {
            "expected": "'product' or 'event'"
          }
        }
      ]
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    await use_case(data.item_id, data.item_type)


@router.post(
    "/generate-pdf/",
    status_code=status.HTTP_200_OK,
    tags=["Servicios"],
    responses={
        200: {
            "description": STATUS_CODE_MESSAGES[200],
            "content": {"application/json": {"example": {}}},
        },
        500: {
            "description": STATUS_CODE_MESSAGES[500],
            "content": {
                "application/json": {"example": {"message": "Data error"}}
            },
        },
    },
)
async def generate_pdf_endpoint(
    use_case: Annotated[
        GetShoppingCartUseCase, Depends(get_shopping_cart_use_case)
    ],
):
    """
    Recurso para generar una factura para el
    carrito de compras.

    **Request Parameters:**

    **Responses:**
    - **200**: Se generó exitosamente.
    - **500**: Error interno del servidor.

    **Example Successful (200):**
    ```json
    {}
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
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

    shopping_cart = ShoppingCartOutput(items=items)

    try:
        pdf_data = generate_pdf_from_cart(shopping_cart)
        return Response(
            content=pdf_data,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=factura.pdf"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
