# Clase que representa un producto del restaurante

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_informacion(self):
        print(self)

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Categoría: {self.categoria}"