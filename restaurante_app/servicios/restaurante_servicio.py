import os

from servicios.archivo_servicio import ArchivoServicio
from modelos.venta import Venta


class RestauranteServicio:

    def __init__(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_productos = os.path.join(base, "datos", "productos.json")
        self.ruta_usuarios = os.path.join(base, "datos", "usuarios.json")
        self.ruta_ventas = os.path.join(base, "datos", "ventas.json")

    # -------------------------
    # USUARIOS
    # -------------------------

    def obtener_usuarios(self):
        return ArchivoServicio.leer_json(self.ruta_usuarios)

    def validar_usuario(self, usuario, password):
        usuarios = self.obtener_usuarios()

        for item in usuarios:
            if item["usuario"] == usuario and item["password"] == password:
                return item

        return None

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def obtener_productos(self):
        return ArchivoServicio.leer_json(self.ruta_productos)

    # -------------------------
    # VENTAS
    # -------------------------

    def obtener_ventas(self):
        return ArchivoServicio.leer_json(self.ruta_ventas)

    def registrar_venta(self, usuario_id, producto_id):
        usuarios = self.obtener_usuarios()
        productos = self.obtener_productos()
        ventas = self.obtener_ventas()

        usuario = next(
            (u for u in usuarios if u["id"] == usuario_id),
            None
        )

        producto = next(
            (p for p in productos if p["id"] == producto_id),
            None
        )

        if usuario is None:
            raise ValueError("El usuario seleccionado no existe.")

        if producto is None:
            raise ValueError("El producto seleccionado no existe.")

        nuevo_id = 1

        if ventas:
            nuevo_id = max(v["id"] for v in ventas) + 1

        venta = Venta(
            id=nuevo_id,
            usuario_id=usuario_id,
            producto_id=producto_id
        )

        ventas.append(venta.to_dict())

        ArchivoServicio.guardar_json(
            self.ruta_ventas,
            ventas
        )

        return venta.to_dict()