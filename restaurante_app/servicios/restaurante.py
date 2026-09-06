from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):
        self.productos = []
        self.usuarios = []
        self.ventas = []

        # Índices para mejorar las búsquedas
        self.productos_por_codigo = {}
        self.usuarios_por_id = {}
        self.ventas_por_usuario = {}

        self.ruta_productos = "datos/productos.json"
        self.ruta_usuarios = "datos/usuarios.json"
        self.ruta_ventas = "datos/ventas.json"

        self.cargar_datos()
        self.reconstruir_indices()

    def cargar_datos(self):
        datos_productos = ArchivoServicio.cargar(self.ruta_productos)

        for dato in datos_productos:
            producto = Producto(
                dato["codigo"],
                dato["nombre"],
                dato["precio"],
                dato["stock"]
            )
            self.productos.append(producto)

        datos_usuarios = ArchivoServicio.cargar(self.ruta_usuarios)

        for dato in datos_usuarios:
            usuario = Usuario(
                dato["identificacion"],
                dato["nombre"]
            )
            self.usuarios.append(usuario)

        datos_ventas = ArchivoServicio.cargar(self.ruta_ventas)

        for dato in datos_ventas:
            venta = Venta(
                dato["identificacion_usuario"],
                dato["codigo_producto"],
                dato["cantidad"]
            )
            self.ventas.append(venta)

    def reconstruir_indices(self):
        self.productos_por_codigo = {}
        self.usuarios_por_id = {}
        self.ventas_por_usuario = {}

        for producto in self.productos:
            self.productos_por_codigo[producto.codigo] = producto

        for usuario in self.usuarios:
            self.usuarios_por_id[usuario.identificacion] = usuario

        for venta in self.ventas:
            if venta.identificacion_usuario not in self.ventas_por_usuario:
                self.ventas_por_usuario[venta.identificacion_usuario] = []

            self.ventas_por_usuario[venta.identificacion_usuario].append(venta)

    def buscar_producto(self, codigo):
        return self.productos_por_codigo.get(codigo)

    def buscar_usuario(self, identificacion):
        return self.usuarios_por_id.get(identificacion)

    def consultar_ventas_usuario(self, identificacion):
        return self.ventas_por_usuario.get(identificacion, [])

    def registrar_producto(self, producto):
        if producto.codigo in self.productos_por_codigo:
            print("El código del producto ya existe.")
            return False

        self.productos.append(producto)
        self.productos_por_codigo[producto.codigo] = producto

        self.guardar_productos()

        return True

    def registrar_usuario(self, usuario):
        if usuario.identificacion in self.usuarios_por_id:
            print("La identificación ya existe.")
            return False

        self.usuarios.append(usuario)
        self.usuarios_por_id[usuario.identificacion] = usuario

        self.guardar_usuarios()

        return True

    def realizar_venta(self, identificacion_usuario, codigo_producto, cantidad):

        usuario = self.usuarios_por_id.get(identificacion_usuario)
        producto = self.productos_por_codigo.get(codigo_producto)

        if usuario is None:
            print("El usuario no existe.")
            return False

        if producto is None:
            print("El producto no existe.")
            return False

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return False

        if producto.stock < cantidad:
            print("No hay suficiente stock.")
            return False

        producto.stock -= cantidad

        venta = Venta(
            identificacion_usuario,
            codigo_producto,
            cantidad
        )

        self.ventas.append(venta)

        if identificacion_usuario not in self.ventas_por_usuario:
            self.ventas_por_usuario[identificacion_usuario] = []

        self.ventas_por_usuario[identificacion_usuario].append(venta)

        self.guardar_productos()
        self.guardar_ventas()

        return True

    def guardar_productos(self):
        datos = []

        for producto in self.productos:
            datos.append({
                "codigo": producto.codigo,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "stock": producto.stock
            })

        ArchivoServicio.guardar(self.ruta_productos, datos)

    def guardar_usuarios(self):
        datos = []

        for usuario in self.usuarios:
            datos.append({
                "identificacion": usuario.identificacion,
                "nombre": usuario.nombre
            })

        ArchivoServicio.guardar(self.ruta_usuarios, datos)

    def guardar_ventas(self):
        datos = []

        for venta in self.ventas:
            datos.append({
                "identificacion_usuario": venta.identificacion_usuario,
                "codigo_producto": venta.codigo_producto,
                "cantidad": venta.cantidad
            })

        ArchivoServicio.guardar(self.ruta_ventas, datos)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def listar_ventas(self):
        for venta in self.ventas:
            print(venta)