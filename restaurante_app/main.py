import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def iniciar():
    MainView(root, servicio)

root = tk.Tk()
root.title("Restaurante App")
root.geometry("700x400")

servicio = RestauranteServicio()

LoginView(root, servicio, iniciar)

root.mainloop()