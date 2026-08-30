from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n========== RESTAURANTE APP ==========")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Registrar usuario")
    print("4. Listar usuarios")
    print("5. Vender producto")
    print("6. Consultar ventas de un usuario")
    print("7. Listar ventas")
    print("8. Salir")
    print("=====================================")


def registrar_producto(restaurante: Restaurante) -> None:
    try:
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))

        if restaurante.registrar_producto(
            codigo,
            nombre,
            precio,
            stock
        ):
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    print("\n---------- PRODUCTOS ----------")

    for producto in productos:
        print(producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    try:
        identificacion = input(
            "Ingrese la identificación del usuario: "
        )

        nombre = input("Ingrese el nombre del usuario: ")

        if restaurante.registrar_usuario(
            identificacion,
            nombre
        ):
            print("Usuario registrado correctamente.")
        else:
            print(
                "Ya existe un usuario con esa identificación."
            )

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    print("\n---------- USUARIOS ----------")

    for usuario in usuarios:
        print(usuario)


def vender_producto(restaurante: Restaurante) -> None:
    try:
        identificacion = input(
            "Ingrese la identificación del usuario: "
        )

        codigo = input(
            "Ingrese el código del producto: "
        )

        cantidad = int(
            input("Ingrese la cantidad a comprar: ")
        )

        if restaurante.vender_producto(
            codigo,
            identificacion,
            cantidad
        ):
            print("\nVenta registrada correctamente.")

            producto = restaurante.buscar_producto(codigo)

            if producto is not None:
                print(
                    f"Stock restante: {producto.stock}"
                )

        else:
            print(
                "No se pudo realizar la venta. "
                "Verifique usuario, producto, cantidad o stock."
            )

    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas_usuario(
    restaurante: Restaurante
) -> None:

    identificacion = input(
        "Ingrese la identificación del usuario: "
    )

    usuario = restaurante.buscar_usuario(
        identificacion
    )

    if usuario is None:
        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(
        identificacion
    )

    if not ventas:
        print(
            "El usuario no tiene ventas registradas."
        )
        return

    print(
        f"\nVentas del usuario: {usuario.nombre}"
    )

    for venta in ventas:

        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        if producto is not None:
            print(
                f"Producto: {producto.nombre} | "
                f"Código: {producto.codigo} | "
                f"Cantidad: {venta.cantidad}"
            )
        else:
            print(venta)


def listar_ventas(restaurante: Restaurante) -> None:
    ventas = restaurante.listar_ventas()

    if not ventas:
        print("No existen ventas registradas.")
        return

    print("\n---------- VENTAS ----------")

    for venta in ventas:

        producto = restaurante.buscar_producto(
            venta.producto_codigo
        )

        usuario = restaurante.buscar_usuario(
            venta.usuario_id
        )

        if producto is not None:
            nombre_producto = producto.nombre
        else:
            nombre_producto = "Producto no encontrado"

        if usuario is not None:
            nombre_usuario = usuario.nombre
        else:
            nombre_usuario = "Usuario no encontrado"

        print(
            f"Usuario: {nombre_usuario} | "
            f"Producto: {nombre_producto} | "
            f"Cantidad: {venta.cantidad}"
        )


def main() -> None:
    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        )

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            registrar_usuario(restaurante)

        elif opcion == "4":
            listar_usuarios(restaurante)

        elif opcion == "5":
            vender_producto(restaurante)

        elif opcion == "6":
            consultar_ventas_usuario(restaurante)

        elif opcion == "7":
            listar_ventas(restaurante)

        elif opcion == "8":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()