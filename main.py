# Archivo principal del programa

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante Sabor Casero")

# Crear productos
producto1 = Producto("Arroz con pollo", 6.50, "Plato fuerte")
producto2 = Producto("Jugo de naranja", 2.00, "Bebida")
producto3 = Producto("Helado", 1.75, "Postre")

# Crear clientes
cliente1 = Cliente("Carlos Pérez", "1723456789", "0991234567")
cliente2 = Cliente("María López", "1712345678", "0987654321")

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("=================================")
print(restaurante.nombre)
print("=================================")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()