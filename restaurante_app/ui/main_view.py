import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, usuario_actual, servicio):
        self.root = root
        self.usuario_actual = usuario_actual
        self.servicio = servicio

        self.root.title("Restaurante App")
        self.root.geometry("1000x650")

        self.crear_interfaz()

    def crear_interfaz(self):
        encabezado = ttk.Frame(self.root, padding=15)
        encabezado.pack(fill="x")

        ttk.Label(
            encabezado,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        ).pack(side="left")

        ttk.Label(
            encabezado,
            text=(
                f"Usuario: {self.usuario_actual.nombre} | "
                f"Rol: {self.usuario_actual.rol}"
            )
        ).pack(side="right")

        menu = ttk.Frame(self.root, padding=15)
        menu.pack(fill="x")

        ttk.Button(
            menu,
            text="Inicio",
            command=self.mostrar_inicio
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Productos",
            command=self.mostrar_productos
        ).pack(side="left", padx=5)

        ttk.Button(
            menu,
            text="Ventas",
            command=self.mostrar_ventas
        ).pack(side="left", padx=5)

        if self.usuario_actual.rol == "Administrador":
            ttk.Button(
                menu,
                text="Usuarios",
                command=self.mostrar_usuarios
            ).pack(side="left", padx=5)

        self.contenido = ttk.Frame(
            self.root,
            padding=20
        )
        self.contenido.pack(fill="both", expand=True)

        self.mostrar_inicio()

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Bienvenido a Restaurante App",
            font=("Arial", 24, "bold")
        ).pack(pady=50)

        ttk.Label(
            self.contenido,
            text="Seleccione una opción del menú."
        ).pack()

    def mostrar_productos(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Productos",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        tabla = ttk.Treeview(
            self.contenido,
            columns=("id", "nombre", "precio", "categoria"),
            show="headings"
        )

        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")
        tabla.heading("categoria", text="Categoría")

        for producto in self.servicio.obtener_productos():
            tabla.insert(
                "",
                "end",
                values=(
                    producto.id_producto,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.categoria
                )
            )

        tabla.pack(fill="both", expand=True)

    def mostrar_ventas(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Ventas",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        ventas = self.servicio.obtener_ventas()

        if not ventas:
            ttk.Label(
                self.contenido,
                text="No existen ventas registradas."
            ).pack(pady=30)
            return

        tabla = ttk.Treeview(
            self.contenido,
            columns=("id", "producto", "cantidad", "total"),
            show="headings"
        )

        for columna, texto in [
            ("id", "ID"),
            ("producto", "Producto"),
            ("cantidad", "Cantidad"),
            ("total", "Total")
        ]:
            tabla.heading(columna, text=texto)

        for venta in ventas:
            tabla.insert(
                "",
                "end",
                values=(
                    venta.id_venta,
                    venta.producto,
                    venta.cantidad,
                    f"${venta.total:.2f}"
                )
            )

        tabla.pack(fill="both", expand=True)

    def mostrar_usuarios(self):
        if self.usuario_actual.rol != "Administrador":
            messagebox.showwarning(
                "Acceso denegado",
                "Solo un Administrador puede gestionar usuarios."
            )
            return

        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Gestión de Usuarios",
            font=("Arial", 22, "bold")
        ).pack(pady=20)

        ttk.Label(
            self.contenido,
            text="Aquí construiremos el CRUD de usuarios."
        ).pack()