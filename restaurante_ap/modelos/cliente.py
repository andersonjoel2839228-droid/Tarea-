from dataclasses import dataclass

@dataclass
class Cliente:
    """Clase que representa un cliente del restaurante."""

    id_cliente: int
    nombre: str
    correo: str

    def mostrar_informacion(self):
        return (
            f"ID: {self.id_cliente} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )