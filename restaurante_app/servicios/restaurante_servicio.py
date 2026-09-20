from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:

    def __init__(self):
        self.ruta_productos = "datos/productos.json"
        self.ruta_usuarios = "datos/usuarios.json"

    def validar_usuario(self, usuario, password):
        usuarios = ArchivoServicio.leer(self.ruta_usuarios)
        for u in usuarios:
            if u["usuario"] == usuario and u["password"] == password:
                return True
        return False

    def obtener_productos(self):
        return ArchivoServicio.leer(self.ruta_productos)

    def registrar_producto(self, producto):
        productos = self.obtener_productos()
        productos.append(producto)
        ArchivoServicio.escribir(self.ruta_productos, productos)

    def eliminar_producto(self, id):
        productos = self.obtener_productos()
        productos = [p for p in productos if p["id"] != id]
        ArchivoServicio.escribir(self.ruta_productos, productos)

    def actualizar_producto(self, id, nuevo):
        productos = self.obtener_productos()
        for p in productos:
            if p["id"] == id:
                p["nombre"] = nuevo["nombre"]
                p["precio"] = nuevo["precio"]
        ArchivoServicio.escribir(self.ruta_productos, productos)