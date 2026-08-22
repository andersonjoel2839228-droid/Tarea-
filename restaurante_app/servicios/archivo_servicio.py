import json
from pathlib import Path
from typing import Any

from modelos.producto import Producto


class ArchivoServicio:
    """Gestiona la lectura y escritura de productos en JSON."""

    def __init__(
        self,
        ruta_archivo: str = "datos/productos.json"
    ) -> None:
        self.ruta_archivo = Path(ruta_archivo)

    def cargar_productos(self) -> list[Producto]:
        """Carga los productos desde el archivo JSON."""

        try:
            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:
                datos: Any = json.load(archivo)

        except FileNotFoundError:
            print("No existe productos.json. Se iniciará sin productos.")
            return []

        except json.JSONDecodeError:
            print(
                "Error: productos.json no contiene un formato JSON válido."
            )
            return []

        except PermissionError:
            print(
                "Error: no hay permisos para leer productos.json."
            )
            return []

        if not isinstance(datos, list):
            print(
                "Error: productos.json debe contener una lista."
            )
            return []

        productos: list[Producto] = []

        for registro in datos:
            try:
                if not isinstance(registro, dict):
                    raise ValueError(
                        "El registro no tiene un formato válido."
                    )

                producto = Producto(
                    nombre=registro["nombre"],
                    precio=float(registro["precio"]),
                    categoria=registro["categoria"]
                )

                productos.append(producto)

            except KeyError as error:
                print(
                    f"Advertencia: falta la clave {error}. "
                    "El producto será ignorado."
                )

            except ValueError as error:
                print(
                    f"Advertencia: producto inválido: {error}. "
                    "El producto será ignorado."
                )

        return productos

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> None:
        """Guarda los productos en el archivo JSON."""

        self.ruta_archivo.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        datos: list[dict[str, Any]] = [
            producto.to_dict()
            for producto in productos
        ]

        try:
            with open(
                self.ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                "Error: no hay permisos para escribir productos.json."
            )