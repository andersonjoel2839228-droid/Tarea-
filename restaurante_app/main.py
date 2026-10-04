import tkinter as tk
from ui.login_view import LoginView


def main():
    root = tk.Tk()
    LoginView(root)
    root.mainloop()