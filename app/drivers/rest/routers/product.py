from typing import Annotated, List

from fastapi import APIRouter, Depends, status

from app.drivers.rest.constants.values import STATUS_CODE_MESSAGES
from app.drivers.rest.dependencies import (
    get_all_products_use_case,
    get_created_product_use_case,
)
from app.drivers.rest.routers.schema import ProductCreate, ProductOutput
from app.use_cases.products.create_product_use_case import CreateProductUseCase
from app.use_cases.products.get_all_products_use_case import (
    GetAllProductsUseCase,
)

router = APIRouter(prefix="/products")


@router.post(
    "/create",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Productos"],
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
                        "message": "The event price must be greater than 0."
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
async def create_product(
    data: ProductCreate,
    use_case: Annotated[
        CreateProductUseCase, Depends(get_created_product_use_case)
    ],
) -> None:
    """
    Recurso para crear un producto.

    **Request Parameters:**
    - price (int): Precio del producto.
    - name (str): Nombre del producto.
    - stock (int): Stock del producto.
    - thumbnail (str): Foto del producto.
    - description (str): Descripción del producto.
    - weight (float): Peso del producto.
    - brand (srt): marca del producto.

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
      "message": "The end date must be greater than the start date."
    }
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    await use_case(data.to_entity())


@router.get(
    "/",
    response_model=List[ProductOutput],
    status_code=status.HTTP_200_OK,
    tags=["Productos"],
    responses={
        200: {
            "description": STATUS_CODE_MESSAGES[200],
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": "20f83a84-24df-46d4-9290-3f6677735cd3",
                            "price": 3232330,
                            "name": "string",
                            "thumbnail": "string",
                            "description": "string",
                            "stock": 30,
                            "weight": 30,
                            "brand": "string",
                        }
                    ]
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
async def get_products(
    use_case: Annotated[
        GetAllProductsUseCase, Depends(get_all_products_use_case)
    ],
) -> List[ProductOutput]:
    """
    Recurso para obtener un producto.

    **Request Parameters:**

    **Responses:**
    - **200**: Se obtuvo exitosamente.
    - **500**: Error interno del servidor.

    **Example Successful (200):**
    ```json
    [
      {
        "id": "20f83a84-24df-46d4-9290-3f6677735cd3",
        "price": 3232330,
        "name": "string",
        "thumbnail": "string",
        "description": "string",
        "stock": 30,
        "weight": 30,
        "brand": "string"
      }
    ]
    ```

    **Example Internal Server Error Response (500):**
    ```json
    {
        "message": "Data error"
    }
    ```
    """
    products = await use_case()
    return products
