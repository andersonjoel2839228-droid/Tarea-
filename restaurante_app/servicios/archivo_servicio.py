import json

class ArchivoServicio:

    @staticmethod
    def leer(ruta):
        try:
            with open(ruta, "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def escribir(ruta, data):
        with open(ruta, "w") as f:
            json.dump(data, f, indent=4)