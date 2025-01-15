import tkinter as tk
from tkinter import PhotoImage


class Home(tk.Frame):
    def __init__(self, master, router, **kwargs):
        super().__init__(master, bg="#1e1e1e", **kwargs)  # Fundo escuro e elegante
        self.router = router  # Armazenando o router
        self.master = master



        # Exibindo as informações em uma linha compacta
        info_frame = tk.Frame(self, bg="#2c2f38", padx=10, pady=10)
        info_frame.pack(pady=20, fill="x", padx=50)

        # Labels com as informações (ID, Nome, Sede, etc) em uma linha compacta
        info_labels = [
            ("ID:", "123"),
            ("Nome:", "NicoCam"),
            ("Sede:", "São Paulo"),
            ("Status:", "Ativo"),
            ("Conexão:", "Estável")
        ]

        # Usando um loop para criar as labels de forma compacta
        for label, value in info_labels:
            tk.Label(info_frame, text=f"{label} {value}", bg="#2c2f38", fg="#bfbfbf", font=("Arial", 12)).pack(
                side="left", padx=20)

        # Espaço para imagem da câmera
        self.imagem_label = tk.Label(self, bg="#1e1e1e", fg="white", width=40, height=20, relief="solid", bd=2)
        self.imagem_label.pack(pady=20)
        self.imagem_label.config(text="Espaço para imagem da câmera")  # Placeholder para imagem da câmera

        # Botões para Rodar Teste e Testar Câmera
        button_frame = tk.Frame(self, bg="#2c2f38")
        button_frame.pack(pady=20)

        # Botão "Rodar Teste"
        rodar_teste_button = tk.Button(
            button_frame, text="Rodar Teste", command=self.rodar_teste, bg="#6C63FF", fg="white",
            font=("Arial", 12, "bold"), relief="raised", padx=25, pady=12, width=18, bd=2
        )
        rodar_teste_button.pack(pady=10)

        # Botão "Testar Câmera"
        testar_camera_button = tk.Button(
            button_frame, text="Testar Câmera", command=self.testar_camera, bg="#6C63FF", fg="white",
            font=("Arial", 12, "bold"), relief="raised", padx=25, pady=12, width=18, bd=2
        )
        testar_camera_button.pack(pady=10)


        # Área de log
        self.log_label = tk.Label(self, text="Última atividade: Nenhuma", bg="#1e1e1e", fg="white", font=("Arial", 12))
        self.log_label.pack(pady=10)

    def rodar_teste(self):
        """Função para rodar o teste (exemplo)."""
        print("Rodando teste...")
        self.atualizar_log("Rodando teste...")

    def testar_camera(self):
        """Função para testar a câmera (exemplo)."""
        print("Testando a câmera...")
        self.atualizar_log("Testando a câmera...")

        # Aqui você pode definir o caminho da imagem ou carregar um vídeo da câmera
        try:
            img = PhotoImage(file="path/to/your/image.png")  # Caminho da imagem da câmera
            self.imagem_label.config(image=img, text="")  # Exibindo a imagem
            self.imagem_label.image = img  # Mantendo a referência da imagem
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            self.imagem_label.config(text="Erro ao carregar a imagem")
            self.atualizar_log(f"Erro ao carregar imagem: {e}")

    def atualizar_log(self, mensagem):
        """Atualiza o log com a nova mensagem."""
        self.log_label.config(text=f"Última atividade: {mensagem}")
