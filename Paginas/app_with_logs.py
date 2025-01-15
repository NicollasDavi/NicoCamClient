import tkinter as tk


class AppWithLogs(tk.Frame):
    def __init__(self, master, router, **kwargs):
        super().__init__(master, bg='#1e1e1e', **kwargs)
        self.router = router
        self.master = master

        # Área para logs
        self.log_frame = tk.Frame(self, bg="#222222", padx=20, pady=10)
        self.log_frame.pack(side="bottom", fill="x", pady=10)

        self.log_text = tk.Label(self.log_frame, text="Logs de Atividades", bg="#333333", fg="white",
                                 font=("Arial", 12))
        self.log_text.pack()

        self.logs = []

    def add_log_message(self, message):
        """Adiciona uma mensagem aos logs e atualiza a tela."""
        self.logs.append(message)

        # Atualizando o texto do log
        log_content = "\n".join(self.logs)
        self.log_text.config(text=log_content)
