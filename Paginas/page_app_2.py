import tkinter as tk

class Pagina2(tk.Frame):
    def __init__(self, master, router, **kwargs):
        super().__init__(master, bg="#333333", **kwargs)
        self.router = router  # Armazenando o router
        self.master = master

        tk.Label(self, text="Página 2", bg="#333333", fg="white", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Voltar para o Menu", command=lambda: self.router.navigate_to("Menu")).pack(pady=10)
