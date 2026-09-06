from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n===== RESTAURANTE APP =====")
    print("1. Registrar usuario")
    print("2. Registrar producto")
    print("3. Buscar usuario")
    print("4. Buscar producto")
    print("5. Realizar venta")
    print("6. Consultar ventas de usuario")
    print("7. Listar usuarios")
    print("8. Listar productos")
    print("9. Listar ventas")
    print("0. Salir")


restaurante = Restaurante()

while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")

        usuario = Usuario(identificacion, nombre)

        if restaurante.registrar_usuario(usuario):
            print("Usuario registrado correctamente.")

    elif opcion == "2":
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        producto = Producto(codigo, nombre, precio, stock)

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")

    elif opcion == "3":
        identificacion = input("Ingrese la identificación: ")

        usuario = restaurante.buscar_usuario(identificacion)

        if usuario:
            print("Usuario encontrado:")
            print(usuario)
        else:
            print("Usuario no encontrado.")

    elif opcion == "4":
        codigo = input("Ingrese el código del producto: ")

        producto = restaurante.buscar_producto(codigo)

        if producto:
            print("Producto encontrado:")
            print(producto)
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        identificacion = input("Identificación del usuario: ")
        codigo = input("Código del producto: ")
        cantidad = int(input("Cantidad: "))

        if restaurante.realizar_venta(
            identificacion,
            codigo,
            cantidad
        ):
            print("Venta realizada correctamente.")
            print("Stock actualizado.")

    elif opcion == "6":
        identificacion = input("Identificación del usuario: ")

        ventas = restaurante.consultar_ventas_usuario(
            identificacion
        )

        if ventas:
            print("\nVentas del usuario:")

            for venta in ventas:
                print(venta)
        else:
            print("No existen ventas para este usuario.")

    elif opcion == "7":
        print("\n===== USUARIOS =====")
        restaurante.listar_usuarios()

    elif opcion == "8":
        print("\n===== PRODUCTOS =====")
        restaurante.listar_productos()

    elif opcion == "9":
        print("\n===== VENTAS =====")
        restaurante.listar_ventas()

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")