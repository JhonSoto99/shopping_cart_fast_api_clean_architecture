from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from app.drivers.rest.routers.schema import ShoppingCartOutput


def generate_pdf_from_cart(cart: ShoppingCartOutput) -> bytes:
    print('******************', cart.items)
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Títulos
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, height - 100, "Factura")

    # Calcular totales
    grand_total = cart.calculate_totals()

    # Tabla
    c.setFont("Helvetica", 10)
    data = [
        ["Nombre del ítem", "Tipo de ítem", "Cantidad", "Precio unitario", "Subtotal"]
    ]

    for item in cart.items:
        subtotal: float = item.price * item.quantity
        data.append(
            [
                item.name,
                item.item_type,
                str(item.quantity),
                f"{item.price:.2f}€",
                f"{subtotal:.2f}€"
            ]
        )

    y = height - 130
    for row in data:
        x = 100
        for col in row:
            c.drawString(x, y, col)
            x += 100
        y -= 15

    # Gran Total
    y -= 20
    c.setFont("Helvetica-Bold", 10)
    c.drawString(100, y, f"Gran Total: {grand_total:.2f}€")

    c.save()
    buffer.seek(0)
    return buffer.getvalue()
