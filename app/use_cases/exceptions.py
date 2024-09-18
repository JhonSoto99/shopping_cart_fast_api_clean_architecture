# app/exceptions.py


class CustomError(Exception):
    """Base class for all custom exceptions"""

    pass


class InvalidProductPriceError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product price must be greater than 0."


class EmptyProductNameError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product name must not be empty."


class EmptyProductThumbnailError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product thumbnail must not be empty."


class EmptyProductDescriptionError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product description must not be empty."


class NegativeStockError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product stock must not be negative."


class NonPositiveWeightError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product weight must be greater than 0."


class EmptyBrandError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "The product brand must not be empty."


class ItemNotFoundError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "Item not found."


class InsufficientStockError(CustomError):
    def __init__(self):
        pass

    def __str__(self) -> str:
        return "Not enough stock for product."
