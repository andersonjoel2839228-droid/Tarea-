import tkinter as tk

class MainView:

    def __init__(self, root, servicio, mostrar_login):
        self.root = root
        self.servicio = servicio
        self.mostrar_login = mostrar_login

        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="PANEL PRINCIPAL").pack()

        tk.Button(self.frame, text="Ver Productos", command=self.ver_productos).pack()
        tk.Button(self.frame, text="Ver Usuarios", command=self.ver_usuarios).pack()
        tk.Button(self.frame, text="Ventas (pendiente)").pack()
        tk.Button(self.frame, text="Cerrar sesión", command=self.logout).pack()

        self.texto = tk.Text(self.frame, height=10, width=40)
        self.texto.pack()

    def ver_productos(self):
        self.texto.delete("1.0", tk.END)
        for p in self.servicio.listar_productos():
            self.texto.insert(tk.END, f"{p.nombre} - ${p.precio} - Stock: {p.stock}\n")

    def ver_usuarios(self):
        self.texto.delete("1.0", tk.END)
        for u in self.servicio.listar_usuarios():
            self.texto.insert(tk.END, f"{u.usuario}\n")

    def logout(self):
        self.frame.destroy()
        self.mostrar_login()