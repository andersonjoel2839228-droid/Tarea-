import tkinter as tk
from tkinter import ttk, messagebox
import os


class MainView:

    def __init__(self, root, servicio, usuario_actual):
        self.root = root
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.root.title("Restaurante App")
        self.root.geometry("950x650")
        self.root.resizable(False, False)

        self.crear_interfaz()
        self.cargar_usuarios()
        self.cargar_productos()
        self.cargar_ventas()

    # =====================================================
    # INTERFAZ PRINCIPAL
    # =====================================================

    def crear_interfaz(self):

        encabezado = tk.Frame(self.root)
        encabezado.pack(fill="x", padx=20, pady=15)

        # -------------------------
        # LOGO
        # -------------------------

        ruta_logo = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets",
            "logo.png"
        )

        try:
            self.logo = tk.PhotoImage(file=ruta_logo)

            logo_label = tk.Label(
                encabezado,
                image=self.logo
            )
            logo_label.pack(side="left", padx=10)

        except Exception:
            pass

        # -------------------------
        # TÍTULO
        # -------------------------

        titulo = tk.Label(
            encabezado,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        )
        titulo.pack(side="left", padx=10)

        nombre = self.usuario_actual.get(
            "nombre",
            "Usuario"
        )

        usuario_label = tk.Label(
            encabezado,
            text=f"Usuario: {nombre}",
            font=("Arial", 11)
        )
        usuario_label.pack(side="right")

        # -------------------------
        # PESTAÑAS
        # -------------------------

        notebook = ttk.Notebook(self.root)
        notebook.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.tab_usuarios = tk.Frame(notebook)
        self.tab_productos = tk.Frame(notebook)
        self.tab_ventas = tk.Frame(notebook)

        notebook.add(
            self.tab_usuarios,
            text="Usuarios"
        )

        notebook.add(
            self.tab_productos,
            text="Productos"
        )

        notebook.add(
            self.tab_ventas,
            text="Ventas"
        )

        self.crear_tab_usuarios()
        self.crear_tab_productos()
        self.crear_tab_ventas()

    # =====================================================
    # USUARIOS
    # =====================================================

    def crear_tab_usuarios(self):

        titulo = tk.Label(
            self.tab_usuarios,
            text="Usuarios registrados",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.tabla_usuarios = ttk.Treeview(
            self.tab_usuarios,
            columns=("id", "nombre", "usuario"),
            show="headings",
            height=15
        )

        self.tabla_usuarios.heading(
            "id",
            text="ID"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla_usuarios.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_usuarios.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabla_usuarios.column(
            "nombre",
            width=300
        )

        self.tabla_usuarios.column(
            "usuario",
            width=200
        )

        self.tabla_usuarios.pack(
            padx=20,
            pady=10
        )

    def cargar_usuarios(self):

        for item in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(item)

        usuarios = self.servicio.obtener_usuarios()

        for usuario in usuarios:
            self.tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario["id"],
                    usuario["nombre"],
                    usuario["usuario"]
                )
            )

    # =====================================================
    # PRODUCTOS
    # =====================================================

    def crear_tab_productos(self):

        titulo = tk.Label(
            self.tab_productos,
            text="Productos disponibles",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.tabla_productos = ttk.Treeview(
            self.tab_productos,
            columns=("id", "nombre", "precio"),
            show="headings",
            height=15
        )

        self.tabla_productos.heading(
            "id",
            text="ID"
        )

        self.tabla_productos.heading(
            "nombre",
            text="Producto"
        )

        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )

        self.tabla_productos.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tabla_productos.column(
            "nombre",
            width=300
        )

        self.tabla_productos.column(
            "precio",
            width=150,
            anchor="center"
        )

        self.tabla_productos.pack(
            padx=20,
            pady=10
        )

    def cargar_productos(self):

        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = self.servicio.obtener_productos()

        for producto in productos:
            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto["id"],
                    producto["nombre"],
                    f"${producto['precio']:.2f}"
                )
            )

    # =====================================================
    # VENTAS
    # =====================================================

    def crear_tab_ventas(self):

        # -------------------------
        # ÍCONO DE VENTAS
        # -------------------------

        ruta_icono = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets",
            "icono_venta.png"
        )

        try:
            self.icono_venta = tk.PhotoImage(
                file=ruta_icono
            )

            icono_label = tk.Label(
                self.tab_ventas,
                image=self.icono_venta
            )

            icono_label.pack(pady=5)

        except Exception:
            pass

        # -------------------------
        # TÍTULO
        # -------------------------

        titulo = tk.Label(
            self.tab_ventas,
            text="Registro de ventas",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=10)

        # -------------------------
        # FORMULARIO
        # -------------------------

        formulario = tk.Frame(
            self.tab_ventas
        )

        formulario.pack(pady=10)

        # USUARIO

        tk.Label(
            formulario,
            text="Usuario:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=8
        )

        self.usuario_combo = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.usuario_combo.grid(
            row=0,
            column=1,
            padx=10,
            pady=8
        )

        # PRODUCTO

        tk.Label(
            formulario,
            text="Producto:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=8
        )

        self.producto_combo = ttk.Combobox(
            formulario,
            state="readonly",
            width=30
        )

        self.producto_combo.grid(
            row=1,
            column=1,
            padx=10,
            pady=8
        )

        # -------------------------
        # BOTÓN REGISTRAR
        # -------------------------

        boton = tk.Button(
            formulario,
            text="Registrar venta",
            width=25,
            command=self.registrar_venta_callback
        )

        boton.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

        # -------------------------
        # TABLA DE VENTAS
        # -------------------------

        self.tabla_ventas = ttk.Treeview(
            self.tab_ventas,
            columns=(
                "id",
                "usuario",
                "producto",
                "fecha"
            ),
            show="headings",
            height=9
        )

        self.tabla_ventas.heading(
            "id",
            text="ID"
        )

        self.tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        self.tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        self.tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        self.tabla_ventas.column(
            "id",
            width=60,
            anchor="center"
        )

        self.tabla_ventas.column(
            "usuario",
            width=180
        )

        self.tabla_ventas.column(
            "producto",
            width=180
        )

        self.tabla_ventas.column(
            "fecha",
            width=200
        )

        self.tabla_ventas.pack(
            padx=20,
            pady=10
        )

        self.cargar_combos()

    # =====================================================
    # COMBOS
    # =====================================================

    def cargar_combos(self):

        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        self.usuarios_data = usuarios
        self.productos_data = productos

        self.usuario_combo["values"] = [
            f"{u['id']} - {u['nombre']}"
            for u in usuarios
        ]

        self.producto_combo["values"] = [
            f"{p['id']} - {p['nombre']}"
            for p in productos
        ]

    # =====================================================
    # CALLBACK DE VENTA
    # =====================================================

    def registrar_venta_callback(self):

        usuario_seleccionado = self.usuario_combo.get()
        producto_seleccionado = self.producto_combo.get()

        if not usuario_seleccionado:

            messagebox.showwarning(
                "Venta",
                "Seleccione un usuario."
            )

            return

        if not producto_seleccionado:

            messagebox.showwarning(
                "Venta",
                "Seleccione un producto."
            )

            return

        usuario_id = int(
            usuario_seleccionado.split(" - ")[0]
        )

        producto_id = int(
            producto_seleccionado.split(" - ")[0]
        )

        try:

            venta = self.servicio.registrar_venta(
                usuario_id,
                producto_id
            )

            self.cargar_ventas()

            messagebox.showinfo(
                "Venta registrada",
                f"La venta #{venta['id']} "
                "fue registrada correctamente."
            )

            self.usuario_combo.set("")
            self.producto_combo.set("")

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # =====================================================
    # CARGAR VENTAS
    # =====================================================

    def cargar_ventas(self):

        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.obtener_ventas()
        usuarios = self.servicio.obtener_usuarios()
        productos = self.servicio.obtener_productos()

        usuarios_dict = {
            u["id"]: u["nombre"]
            for u in usuarios
        }

        productos_dict = {
            p["id"]: p["nombre"]
            for p in productos
        }

        for venta in ventas:

            usuario_nombre = usuarios_dict.get(
                venta["usuario_id"],
                "Desconocido"
            )

            producto_nombre = productos_dict.get(
                venta["producto_id"],
                "Desconocido"
            )

            self.tabla_ventas.insert(
                "",
                "end",
                values=(
                    venta["id"],
                    usuario_nombre,
                    producto_nombre,
                    venta["fecha"]
                )
            )