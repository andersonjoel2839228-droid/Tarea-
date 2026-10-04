import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root):
        self.root = root

        self.root.title("Restaurante App - Inicio de sesión")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        titulo = tk.Label(
            root,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=30)

        tk.Label(
            root,
            text="Usuario:"
        ).pack()

        self.usuario = tk.Entry(root, width=35)
        self.usuario.pack(pady=5)

        tk.Label(
            root,
            text="Contraseña:"
        ).pack()

        self.contraseña = tk.Entry(
            root,
            width=35,
            show="*"
        )
        self.contraseña.pack(pady=5)

        tk.Button(
            root,
            text="Ingresar",
            width=20,
            command=self.iniciar_sesion
        ).pack(pady=25)

        self.usuario.focus()

    def iniciar_sesion(self):
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()

        if usuario == "admin" and contraseña == "admin123":
            messagebox.showinfo(
                "Correcto",
                "Inicio de sesión correcto"
            )
        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos"
            )