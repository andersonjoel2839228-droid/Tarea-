# Tarea-
Ejercitación 
# Programa: Registro de productos de una tienda usando lista

productos = []

def agregar_producto():
    nombre = input("Ingrese el producto: ")
    productos.append(nombre)
    print("Producto agregado\n")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados\n")
    else:
        print("Lista de productos:")
        for p in productos:
            print("-", p)
        print()

def buscar_producto():
    nombre = input("Producto a buscar: ")
    if nombre in productos:
        print("Producto encontrado\n")
    else:
        print("No encontrado\n")

def eliminar_producto():
    nombre = input("Producto a eliminar: ")
    if nombre in productos:
        productos.remove(nombre)
        print("Producto eliminado\n")
    else:
        print("No encontrado\n")

while True:
    print("=== MENÚ ===")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        break
        
