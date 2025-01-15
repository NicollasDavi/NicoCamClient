class Router:
    def __init__(self, master):
        self.master = master
        self.frames = {}
        self.current_frame = None

    def add_route(self, route, frame_class):
        """Adiciona uma rota para o sistema de navegação."""
        self.frames[route] = frame_class(self.master, self)  # Passando o 'router' como argumento

    def navigate_to(self, route):
        """Exibe a página ou frame de acordo com a rota."""
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[route]
        self.current_frame.pack(fill="both", expand=True)
