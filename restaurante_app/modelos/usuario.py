class Usuario:
    """Representa un usuario del sistema."""

    def __init__(
        self,
        nombre: str,
        correo: str
    ) -> None:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        if not correo.strip():
            raise ValueError("El correo no puede estar vacío.")

        self.nombre = nombre.strip()
        self.correo = correo.strip()

    def __str__(self) -> str:
        return (
            f"Usuario: {self.nombre} | "
            f"Correo: {self.correo}"
        )