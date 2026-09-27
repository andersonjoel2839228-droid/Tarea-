from datetime import datetime


class Venta:
    def __init__(self, id, usuario_id, producto_id, fecha=None):
        self.id = id
        self.usuario_id = usuario_id
        self.producto_id = producto_id
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "producto_id": self.producto_id,
            "fecha": self.fecha
        }