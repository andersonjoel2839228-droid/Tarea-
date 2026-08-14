from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


restaurante = Restaurante()


def registrar_producto() -> None:
    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese el código: ").strip()
    nombre = input("Ingrese el nombre: ").strip()
    categoria = input("Ingrese la categoría: ").strip()

    try:
        precio = float(input("Ingrese el precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("Error: debe ingresar un precio válido.")
        return

    producto = Producto(codigo, nombre, categoria, precio)

    if restaurante.registrar_producto(producto):
        print("Producto registrado correctamente.")
    else:
        print("Error: ya existe un producto con ese código.")


def buscar_producto() -> None:
    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()
    producto = restaurante.buscar_producto(codigo)

    if producto is not None:
        print("\nProducto encontrado:")
        print(producto)
    else:
        print("No se encontró ningún producto con ese código.")


def actualizar_producto() -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("No existe un producto con ese código.")
        return

    nombre = input("Nuevo nombre: ").strip()
    categoria = input("Nueva categoría: ").strip()

    try:
        precio = float(input("Nuevo precio: "))

        if precio < 0:
            print("El precio no puede ser negativo.")
            return

    except ValueError:
        print("Error: debe ingresar un precio válido.")
        return

    restaurante.actualizar_producto(
        codigo,
        nombre,
        categoria,
        precio
    )

    print("Producto actualizado correctamente.")


def eliminar_producto() -> None:
    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    if restaurante.eliminar_producto(codigo):
        print("Producto eliminado correctamente.")
    else:
        print("No existe un producto con ese código.")


def listar_productos() -> None:
    print("\n--- LISTA DE PRODUCTOS ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario() -> None:
    print("\n--- REGISTRAR USUARIO ---")

    identificacion = input("Ingrese la identificación: ").strip()
    nombre = input("Ingrese el nombre: ").strip()
    correo = input("Ingrese el correo: ").strip()

    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_usuario(usuario):
        print("Usuario registrado correctamente.")
    else:
        print("Error: ya existe un usuario con esa identificación.")


def listar_usuarios() -> None:
    print("\n--- LISTA DE USUARIOS ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def mostrar_categorias() -> None:
    print("\n--- CATEGORÍAS ---")

    categorias = restaurante.obtener_categorias()

    if not categorias:
        print("No existen categorías registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def salir() -> None:
    print("\nGracias por utilizar el sistema de restaurante.")


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("----------------------------------------")
    print("6. Registrar usuario")
    print("7. Listar usuarios")
    print("----------------------------------------")
    print("8. Mostrar categorías")
    print("9. Salir")
    print("========================================")


def ejecutar_programa() -> None:
    opciones_menu: tuple[str, ...] = (
        "1", "2", "3", "4", "5",
        "6", "7", "8", "9"
    )

    acciones = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
        "9": salir
    }

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion not in opciones_menu:
            print("Opción no válida.")
            continue

        acciones[opcion]()

        if opcion == "9":
            break


if __name__ == "__main__":
    ejecutar_programa()