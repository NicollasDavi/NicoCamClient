import tkinter as tk
from Components.app_bar import AppBar
from Paginas.page_app_login import Login
from Paginas.page_app_home import Home
from Paginas.page_app_2 import Pagina2
from Utils.router import Router

window = tk.Tk()
window.title("NicoCam")
window.geometry("1720x900")
window.configure(bg='#1e1e1e')
window.overrideredirect(True)

# AppBar no topo (não será empurrada)
AppBar(window).pack(side="top", fill="x")

# Inicializando o Router
router = Router(window)

# Adicionando as páginas ao router
router.add_route("Login", Login)
router.add_route("Home", Home)  # Página 1
router.add_route("Pagina2", Pagina2)  # Página 2

# Exibindo a página de Login inicial
router.navigate_to("Login")

window.mainloop()