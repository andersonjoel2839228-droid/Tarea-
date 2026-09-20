import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root, servicio, on_login):
        self.root = root
        self.servicio = servicio
        self.on_login = on_login

        self.frame = tk.Frame(root)
        self.frame.pack(pady=50)

        tk.Label(self.frame, text="Usuario").pack()
        self.usuario = tk.Entry(self.frame)
        self.usuario.pack()

        tk.Label(self.frame, text="Contraseña").pack()
        self.password = tk.Entry(self.frame, show="*")
        self.password.pack()

        tk.Button(self.frame, text="Ingresar", command=self.login).pack(pady=10)

    def login(self):
        if self.servicio.validar_usuario(
            self.usuario.get(),
            self.password.get()
        ):
            self.frame.destroy()
            self.on_login()
        else:
            messagebox.showerror("Error", "Datos incorrectos")