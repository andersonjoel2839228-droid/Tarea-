import tkinter as tk

class LoginView:

    def __init__(self, root, servicio, mostrar_main):
        self.root = root
        self.servicio = servicio
        self.mostrar_main = mostrar_main

        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="LOGIN").pack()

        tk.Label(self.frame, text="Usuario").pack()
        self.usuario = tk.Entry(self.frame)
        self.usuario.pack()

        tk.Label(self.frame, text="Contraseña").pack()
        self.password = tk.Entry(self.frame, show="*")
        self.password.pack()

        self.mensaje = tk.Label(self.frame, text="", fg="red")
        self.mensaje.pack()

        tk.Button(self.frame, text="Ingresar", command=self.login).pack()

    def login(self):
        user = self.usuario.get()
        pwd = self.password.get()

        if not user or not pwd:
            self.mensaje.config(text="Campos vacíos")
            return

        if self.servicio.validar_usuario(user, pwd):
            self.frame.destroy()
            self.mostrar_main()
        else:
            self.mensaje.config(text="Datos incorrectos")