import json
import os


class ArchivoServicio:

    @staticmethod
    def guardar(ruta, datos):
        carpeta = os.path.dirname(ruta)

        if carpeta:
            os.makedirs(carpeta, exist_ok=True)

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)

    @staticmethod
    def cargar(ruta):
        if not os.path.exists(ruta):
            return []

        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)