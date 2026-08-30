from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        self._ruta_productos = "datos/productos.json"
        self._ruta_usuarios = "datos/usuarios.json"
        self._ruta_ventas = "datos/ventas.json"

        self.cargar_datos()

    # =========================
    # PRODUCTOS
    # =========================

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        precio: float,
        stock: int
    ) -> bool:

        if self.buscar_producto(codigo) is not None:
            return False

        producto = Producto(
            codigo,
            nombre,
            precio,
            stock
        )

        self._productos.append(producto)
        self.guardar_productos()

        return True

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def guardar_productos(self) -> None:
        datos = []

        for producto in self._productos:
            datos.append(
                producto.convertir_a_diccionario()
            )

        ArchivoServicio.guardar(
            self._ruta_productos,
            datos
        )

    # =========================
    # USUARIOS
    # =========================

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str
    ) -> bool:

        if self.buscar_usuario(identificacion) is not None:
            return False

        usuario = Usuario(
            identificacion,
            nombre
        )

        self._usuarios.append(usuario)
        self.guardar_usuarios()

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def guardar_usuarios(self) -> None:
        datos = []

        for usuario in self._usuarios:
            datos.append(
                usuario.convertir_a_diccionario()
            )

        ArchivoServicio.guardar(
            self._ruta_usuarios,
            datos
        )

    # =========================
    # VENTAS
    # =========================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        producto = self.buscar_producto(
            codigo_producto
        )

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        self.guardar_ventas()
        self.guardar_productos()

        return True

    def consultar_ventas_usuario(
        self,
        identificacion_usuario: str
    ) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        return self._ventas

    def guardar_ventas(self) -> None:
        datos = []

        for venta in self._ventas:
            datos.append(
                venta.convertir_a_diccionario()
            )

        ArchivoServicio.guardar(
            self._ruta_ventas,
            datos
        )

    # =========================
    # CARGAR DATOS
    # =========================

    def cargar_datos(self) -> None:

        # Cargar productos
        datos_productos = ArchivoServicio.cargar(
            self._ruta_productos
        )

        for datos in datos_productos:
            try:
                producto = Producto.desde_diccionario(
                    datos
                )

                self._productos.append(producto)

            except (KeyError, ValueError) as error:
                print(
                    f"Error al cargar producto: {error}"
                )

        # Cargar usuarios
        datos_usuarios = ArchivoServicio.cargar(
            self._ruta_usuarios
        )

        for datos in datos_usuarios:
            try:
                usuario = Usuario.desde_diccionario(
                    datos
                )

                self._usuarios.append(usuario)

            except (KeyError, ValueError) as error:
                print(
                    f"Error al cargar usuario: {error}"
                )

        # Cargar ventas
        datos_ventas = ArchivoServicio.cargar(
            self._ruta_ventas
        )

        for datos in datos_ventas:
            try:
                venta = Venta.desde_diccionario(
                    datos
                )

                self._ventas.append(venta)

            except (KeyError, ValueError) as error:
                print(
                    f"Error al cargar venta: {error}"
                )