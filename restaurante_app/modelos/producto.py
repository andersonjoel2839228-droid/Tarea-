class Producto:
    """Representa un producto del restaurante."""

    def __init__(
        self,
        nombre: str,
        precio: float,
        categoria: str
    ) -> None:
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        self.nombre = nombre.strip()
        self.precio = precio
        self.categoria = categoria.strip()

    def to_dict(self) -> dict[str, str | float]:
        """Convierte el producto en un diccionario para guardarlo en JSON."""
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria
        }

    def __str__(self) -> str:
        return (
            f"Producto: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Categoría: {self.categoria}"
        )