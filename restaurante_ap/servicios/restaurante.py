from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """Clase que administra los productos y clientes."""

    def __init__(self):
        self.productos = []
        self.clientes = []

    # -------- PRODUCTOS --------
    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        if not self.productos:
            print("\nNo hay productos registrados.")
        else:
            print("\n=== LISTA DE PRODUCTOS ===")
            for producto in self.productos:
                print(producto.mostrar_informacion())

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    # -------- CLIENTES --------
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("\nNo hay clientes registrados.")
        else:
            print("\n=== LISTA DE CLIENTES ===")
            for cliente in self.clientes:
                print(cliente.mostrar_informacion())

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None