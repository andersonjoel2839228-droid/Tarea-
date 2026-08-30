import json
import os


class ArchivoServicio:

    @staticmethod
    def guardar(ruta: str, datos: list[dict]) -> None:
        try:
            os.makedirs(os.path.dirname(ruta), exist_ok=True)

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print(
                f"Error: no hay permisos para escribir en {ruta}."
            )

    @staticmethod
    def cargar(ruta: str) -> list[dict]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                if not isinstance(datos, list):
                    raise ValueError(
                        f"El archivo {ruta} debe contener una lista."
                    )

                return datos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                f"Error: el archivo {ruta} contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                f"Error: no hay permisos para leer {ruta}."
            )
            return []

        except ValueError as error:
            print(f"Error en el archivo {ruta}: {error}")
            return []