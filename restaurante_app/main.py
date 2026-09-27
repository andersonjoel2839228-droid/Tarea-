import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def mostrar_principal(usuario):
    for widget in root.winfo_children():
        widget.destroy()

    MainView(
        root,
        servicio,
        usuario
    )


servicio = RestauranteServicio()

root = tk.Tk()

LoginView(
    root,
    servicio,
    mostrar_principal
)

root.mainloop()