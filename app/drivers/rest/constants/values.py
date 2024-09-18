API_V1_PREFIX: str = "/api/v1"
"""Versión 1 de la api."""

STATUS_CODE_MESSAGES: dict = {
    200: "Successful Response",
    204: "Successful Not Content",
    400: "Validation Error.",
    422: "Error: Unprocessable Entity.",
    500: "Internal Server Error. Please try again later.",
}
"""STATUS_CODE_MESSAGES: Contiene los mensajes predefinidos para los
posibles códigos de estado de respuesta."""
