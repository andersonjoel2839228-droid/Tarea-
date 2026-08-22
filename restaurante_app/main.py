from modelos.producto import Producto
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    """Muestra las opciones principales del sistema."""
    print("\n========== RESTAURANTE APP ==========")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("======================================")


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    """Solicita datos y registra un producto."""
    try:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        categoria = input("Categoría: ")

        producto = Producto(
            nombre=nombre,
            precio=precio,
            categoria=categoria
        )

        restaurante.registrar_producto(producto)
        archivo_servicio.guardar_productos(
            restaurante.listar_productos()
        )

        print("Producto registrado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    """Muestra todos los productos registrados."""
    productos = restaurante.listar_productos()

    if not productos:
        print("\nNo hay productos registrados.")
        return

    print("\n========== PRODUCTOS ==========")

    for producto in productos:
        print(producto)


def buscar_producto(restaurante: Restaurante) -> None:
    """Busca un producto por su nombre."""
    nombre = input("Ingrese el nombre del producto: ")

    producto = restaurante.buscar_producto(nombre)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print("\nProducto encontrado:")
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    """Actualiza un producto existente."""
    nombre_actual = input(
        "Ingrese el nombre del producto que desea actualizar: "
    )

    producto = restaurante.buscar_producto(nombre_actual)

    if producto is None:
        print("Producto no encontrado.")
        return

    try:
        nuevo_nombre = input("Nuevo nombre: ")
        nuevo_precio = float(input("Nuevo precio: "))
        nueva_categoria = input("Nueva categoría: ")

        actualizado = restaurante.actualizar_producto(
            nombre_actual,
            nuevo_nombre,
            nuevo_precio,
            nueva_categoria
        )

        if actualizado:
            archivo_servicio.guardar_productos(
                restaurante.listar_productos()
            )
            print("Producto actualizado correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio
) -> None:
    """Elimina un producto."""
    nombre = input("Ingrese el nombre del producto a eliminar: ")

    eliminado = restaurante.eliminar_producto(nombre)

    if eliminado:
        archivo_servicio.guardar_productos(
            restaurante.listar_productos()
        )
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def main() -> None:
    """Función principal del programa."""
    restaurante = Restaurante()
    archivo_servicio = ArchivoServicio()

    productos_guardados = archivo_servicio.cargar_productos()
    restaurante.cargar_productos(productos_guardados)

    print("Productos cargados correctamente.")

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            buscar_producto(restaurante)

        elif opcion == "4":
            actualizar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "5":
            eliminar_producto(
                restaurante,
                archivo_servicio
            )

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()