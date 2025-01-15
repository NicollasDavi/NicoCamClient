import tkinter as tk

class AppBar(tk.Frame):
    def __init__(self, master, titulo="NicoCam Client", bg="#1e1e1e", fg="white", hover_color="#555555", **kwargs):
        super().__init__(master, bg=bg, **kwargs)
        self.master = master
        self.bg = bg
        self.fg = fg
        self._hover_color = hover_color

        # Título
        self.titulo = tk.Label(self, text=titulo, bg=bg, fg=fg, font=("Arial", 12, "bold"))
        self.titulo.pack(side="left", padx=10)

        # Botão de fechar
        self.botao_fechar = tk.Button(self, text="X", bg=bg, fg=fg, font=("Arial", 10, "bold"), borderwidth=0, command=self.fechar)
        self.botao_fechar.pack(side="right", padx=5)

        # Efeito de hover no botão
        self.botao_fechar.bind("<Enter>", lambda e: self._hover_botao(self.botao_fechar, True))
        self.botao_fechar.bind("<Leave>", lambda e: self._hover_botao(self.botao_fechar, False))
        self.botao_fechar.bind("<Button-1>", lambda e: self.fechar())

        # Variáveis para calcular o movimento
        self.offset_x = 0
        self.offset_y = 0

        # Tornar a barra arrastável
        self.bind("<ButtonPress-1>", self.iniciar_arraste)
        self.bind("<B1-Motion>", self.mover)

    def _hover_botao(self, widget, entrar):
        """Alterar a cor do botão no hover."""
        if entrar:
            widget.config(bg=self._hover_color)
        else:
            widget.config(bg=self.bg)

    def fechar(self):
        """Fecha a janela principal."""
        self.master.destroy()

    def iniciar_arraste(self, event):
        """Captura a posição do mouse quando o clique é feito."""
        self.offset_x = event.x
        self.offset_y = event.y

    def mover(self, event):
        """Move a janela com base no movimento do mouse."""
        x = self.master.winfo_x() + event.x - self.offset_x
        y = self.master.winfo_y() + event.y - self.offset_y
        self.master.geometry(f"+{x}+{y}")
