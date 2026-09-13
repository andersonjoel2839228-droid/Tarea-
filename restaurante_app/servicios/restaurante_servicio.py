from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:

    def __init__(self):
        usuarios_data = ArchivoServicio.leer_json("datos/usuarios.json")
        productos_data = ArchivoServicio.leer_json("datos/productos.json")

        self.usuarios = [Usuario(**u) for u in usuarios_data]
        self.productos = [Producto(**p) for p in productos_data]

    def validar_usuario(self, usuario, password):
        for u in self.usuarios:
            if u.usuario == usuario and u.password == password:
                return True
        return False

    def listar_usuarios(self):
        return self.usuarios

    def listar_productos(self):
        return self.productos