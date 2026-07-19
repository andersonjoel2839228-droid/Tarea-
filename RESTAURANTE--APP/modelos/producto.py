class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Cantidad: {self.cantidad} - Disponible: {self.disponible}"