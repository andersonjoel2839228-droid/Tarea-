import tkinter as tk
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def main():
    root = tk.Tk()
    root.title("Restaurante App")

    servicio = RestauranteServicio()

    def mostrar_main():
        MainView(root, servicio, mostrar_login)

    def mostrar_login():
        LoginView(root, servicio, mostrar_main)

    mostrar_login()

    root.mainloop()

if __name__ == "__main__":
    main()