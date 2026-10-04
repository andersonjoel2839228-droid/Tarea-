import os

from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        self.ruta_usuarios = os.path.join(
            base, "datos", "usuarios.json"
        )

        self.ruta_productos = os.path.join(
            base, "datos", "productos.json"
        )

        self.ruta_ventas = os.path.join(
            base, "datos", "ventas.json"
        )

    # =========================
    # USUARIOS
    # =========================

    def obtener_usuarios(self):
        datos = ArchivoServicio.leer_json(self.ruta_usuarios)

        return [
            Usuario.from_dict(usuario)
            for usuario in datos
        ]

    def buscar_usuario_por_id(self, id_usuario):
        usuarios = self.obtener_usuarios()

        for usuario in usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario

        return None

    def buscar_usuario_por_nombre_usuario(self, nombre_usuario):
        usuarios = self.obtener_usuarios()

        for usuario in usuarios:
            if usuario.usuario.lower() == nombre_usuario.lower():
                return usuario

        return None

    def iniciar_sesion(self, nombre_usuario, contraseña):
        usuario = self.buscar_usuario_por_nombre_usuario(nombre_usuario)

        if usuario is None:
            return None

        if usuario.contraseña != contraseña:
            return None

        return usuario

    def registrar_usuario(self, nombre, usuario, contraseña, rol):
        nombre = nombre.strip()
        usuario = usuario.strip()
        contraseña = contraseña.strip()
        rol = rol.strip()

        if not nombre or not usuario or not contraseña or not rol:
            return False, "Todos los campos son obligatorios."

        if rol not in ["Administrador", "Empleado", "Cliente"]:
            return False, "El rol seleccionado no es válido."

        if self.buscar_usuario_por_nombre_usuario(usuario):
            return False, "El nombre de usuario ya existe."

        usuarios = self.obtener_usuarios()

        nuevo_id = 1

        if usuarios:
            nuevo_id = max(
                u.id_usuario for u in usuarios
            ) + 1

        nuevo_usuario = Usuario(
            nuevo_id,
            nombre,
            usuario,
            contraseña,
            rol
        )

        usuarios.append(nuevo_usuario)

        datos = [
            u.to_dict()
            for u in usuarios
        ]

        ArchivoServicio.guardar_json(
            self.ruta_usuarios,
            datos
        )

        return True, "Usuario registrado correctamente."

    def actualizar_usuario(
        self,
        id_usuario,
        nombre,
        usuario,
        contraseña,
        rol
    ):
        nombre = nombre.strip()
        usuario = usuario.strip()
        contraseña = contraseña.strip()
        rol = rol.strip()

        if not nombre or not usuario or not contraseña or not rol:
            return False, "Todos los campos son obligatorios."

        if rol not in ["Administrador", "Empleado", "Cliente"]:
            return False, "El rol seleccionado no es válido."

        usuarios = self.obtener_usuarios()

        usuario_encontrado = None

        for u in usuarios:
            if u.id_usuario == id_usuario:
                usuario_encontrado = u

            elif u.usuario.lower() == usuario.lower():
                return False, "Ese nombre de usuario ya está registrado."

        if usuario_encontrado is None:
            return False, "Usuario no encontrado."

        usuario_encontrado.nombre = nombre
        usuario_encontrado.usuario = usuario
        usuario_encontrado.contraseña = contraseña
        usuario_encontrado.rol = rol

        datos = [
            u.to_dict()
            for u in usuarios
        ]

        ArchivoServicio.guardar_json(
            self.ruta_usuarios,
            datos
        )

        return True, "Usuario actualizado correctamente."

    def eliminar_usuario(self, id_usuario, id_usuario_actual):
        if id_usuario == id_usuario_actual:
            return False, "No puedes eliminar el usuario actualmente autenticado."

        usuarios = self.obtener_usuarios()

        usuario_encontrado = None

        for usuario in usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_encontrado = usuario
                break

        if usuario_encontrado is None:
            return False, "Usuario no encontrado."

        if usuario_encontrado.rol == "Administrador":
            administradores = [
                u for u in usuarios
                if u.rol == "Administrador"
            ]

            if len(administradores) <= 1:
                return False, "Debe existir al menos un Administrador."

        usuarios.remove(usuario_encontrado)

        datos = [
            u.to_dict()
            for u in usuarios
        ]

        ArchivoServicio.guardar_json(
            self.ruta_usuarios,
            datos
        )

        return True, "Usuario eliminado correctamente."

    # =========================
    # PRODUCTOS
    # =========================

    def obtener_productos(self):
        datos = ArchivoServicio.leer_json(self.ruta_productos)

        return [
            Producto.from_dict(producto)
            for producto in datos
        ]

    # =========================
    # VENTAS
    # =========================

    def obtener_ventas(self):
        datos = ArchivoServicio.leer_json(self.ruta_ventas)

        return [
            Venta.from_dict(venta)
            for venta in datos
        ]