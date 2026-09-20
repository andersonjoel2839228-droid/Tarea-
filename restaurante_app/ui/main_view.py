import tkinter as tk
from tkinter import ttk

class MainView:

    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        # CONTENEDOR PRINCIPAL
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True)

        # MENÚ
        self.menu = tk.Frame(self.frame, bg="#34495e", width=150)
        self.menu.pack(side="left", fill="y")

        # CONTENIDO
        self.contenido = tk.Frame(self.frame)
        self.contenido.pack(side="right", fill="both", expand=True)

        tk.Button(self.menu, text="Productos", command=self.vista_productos).pack(fill="x")

        self.vista_productos()

    def limpiar(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    def vista_productos(self):
        self.limpiar()

        # FORMULARIO
        form = tk.LabelFrame(self.contenido, text="Formulario")
        form.pack(side="left", fill="y", padx=10, pady=10)

        tk.Label(form, text="ID").pack()
        self.id = tk.Entry(form)
        self.id.pack()

        tk.Label(form, text="Nombre").pack()
        self.nombre = tk.Entry(form)
        self.nombre.pack()

        tk.Label(form, text="Precio").pack()
        self.precio = tk.Entry(form)
        self.precio.pack()

        tk.Button(form, text="Registrar", command=self.registrar).pack(pady=5)
        tk.Button(form, text="Actualizar", command=self.actualizar).pack(pady=5)
        tk.Button(form, text="Eliminar", command=self.eliminar).pack(pady=5)

        # TABLA
        tabla_frame = tk.LabelFrame(self.contenido, text="Lista")
        tabla_frame.pack(side="right", fill="both", expand=True)

        self.tabla = ttk.Treeview(tabla_frame, columns=("id","nombre","precio"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio")
        self.tabla.pack(fill="both", expand=True)

        self.cargar()

    def cargar(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for p in self.servicio.obtener_productos():
            self.tabla.insert("", "end", values=(p["id"], p["nombre"], p["precio"]))

    def registrar(self):
        producto = {
            "id": self.id.get(),
            "nombre": self.nombre.get(),
            "precio": self.precio.get()
        }
        self.servicio.registrar_producto(producto)
        self.cargar()

    def actualizar(self):
        nuevo = {
            "nombre": self.nombre.get(),
            "precio": self.precio.get()
        }
        self.servicio.actualizar_producto(self.id.get(), nuevo)
        self.cargar()

    def eliminar(self):
        self.servicio.eliminar_producto(self.id.get())
        self.cargar()