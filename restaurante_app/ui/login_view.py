import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_principal):
        self.root = root
        self.servicio = servicio
        self.mostrar_principal = mostrar_principal

        self.root.title("Restaurante App - Inicio de sesión")
        self.root.geometry("420x350")
        self.root.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        titulo = tk.Label(
            self.root,
            text="RESTAURANTE APP",
            font=("Arial", 22, "bold")
        )
        titulo.pack(pady=(40, 10))

        subtitulo = tk.Label(
            self.root,
            text="Inicio de sesión",
            font=("Arial", 13)
        )
        subtitulo.pack(pady=5)

        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        tk.Label(
            frame,
            text="Usuario:"
        ).grid(row=0, column=0, padx=10, pady=10)

        self.usuario_entry = tk.Entry(frame, width=25)
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(
            frame,
            text="Contraseña:"
        ).grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(
            frame,
            width=25,
            show="*"
        )
        self.password_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        boton = tk.Button(
            self.root,
            text="Iniciar sesión",
            width=20,
            command=self.iniciar_sesion
        )
        boton.pack(pady=15)

        self.usuario_entry.focus()

    def iniciar_sesion(self):

        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese usuario y contraseña."
            )
            return

        resultado = self.servicio.validar_usuario(
            usuario,
            password
        )

        if resultado:
            self.mostrar_principal(resultado)
        else:
            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )