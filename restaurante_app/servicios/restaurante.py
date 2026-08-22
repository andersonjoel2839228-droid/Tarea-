from modelos.producto import Producto


class Restaurante:
    """Administra los productos del restaurante."""

    def __init__(self) -> None:
        self._productos: list[Producto] = []

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un nuevo producto."""
        self._productos.append(producto)

    def listar_productos(self) -> list[Producto]:
        """Devuelve la lista de productos."""
        return self._productos.copy()

    def buscar_producto(self, nombre: str) -> Producto | None:
        """Busca un producto por su nombre."""
        for producto in self._productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    def actualizar_producto(
        self,
        nombre_actual: str,
        nuevo_nombre: str,
        nuevo_precio: float,
        nueva_categoria: str
    ) -> bool:
        """Actualiza los datos de un producto."""
        producto = self.buscar_producto(nombre_actual)

        if producto is None:
            return False

        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if not nueva_categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        producto.nombre = nuevo_nombre.strip()
        producto.precio = nuevo_precio
        producto.categoria = nueva_categoria.strip()

        return True

    def eliminar_producto(self, nombre: str) -> bool:
        """Elimina un producto por su nombre."""
        producto = self.buscar_producto(nombre)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def cargar_productos(self, productos: list[Producto]) -> None:
        """Carga productos recuperados desde el archivo JSON."""
        self._productos = productos.copy()