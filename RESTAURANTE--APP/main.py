from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

restaurante = Restaurante("Restaurante Sabor Latino")

producto1 = Producto("Hamburguesa", 5.50, 20, True)
producto2 = Producto("Pizza", 8.00, 10, True)

cliente1 = Cliente("Juan Pérez", 20, "0991111111", True)
cliente2 = Cliente("María López", 22, "0992222222", True)

restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

print(restaurante.nombre)
print("----------------------------")
restaurante.mostrar_productos()
print("----------------------------")
restaurante.mostrar_clientes()