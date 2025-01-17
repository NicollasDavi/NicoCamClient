# Arquivo: main.py ou Home.py
import tkinter as tk
import threading
from Utils.CameraUtils.camera_utils import start_camera_stream
from Utils.move_servo import move_servo


class Home(tk.Frame):
    def __init__(self, master, router, **kwargs):
        super().__init__(master, bg="#1e1e1e", **kwargs)
        self.router = router
        self.master = master
        self.stop_camera_flag = False

        # Exibindo as informações
        info_frame = tk.Frame(self, bg="#2c2f38", padx=10, pady=10)
        info_frame.pack(pady=20, fill="x", padx=50)

        info_labels = [
            ("ID:", "123"),
            ("Nome:", "NicoCam"),
            ("Sede:", "São Paulo"),
            ("Status:", "Ativo"),
            ("Conexão:", "Estável")
        ]

        for label, value in info_labels:
            tk.Label(info_frame, text=f"{label} {value}", bg="#2c2f38", fg="#bfbfbf", font=("Arial", 12)).pack(
                side="left", padx=20)

        # Área maior para o feed da câmera
        self.imagem_label = tk.Label(self, bg="#1e1e1e", relief="solid", bd=2)
        self.imagem_label.pack(pady=20, fill="both", expand=True)  # Expande conforme o tamanho da janela
        self.imagem_label.config(text="Espaço para imagem da câmera")

        # Botões
        button_frame = tk.Frame(self, bg="#2c2f38")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame, text="Rodar Teste", command=self.rodar_teste, bg="#6C63FF", fg="white",
            font=("Arial", 12, "bold"), relief="raised", padx=25, pady=12, width=18, bd=2
        ).pack(pady=10)

        tk.Button(
            button_frame, text="Testar Câmera", command=self.testar_camera, bg="#6C63FF", fg="white",
            font=("Arial", 12, "bold"), relief="raised", padx=25, pady=12, width=18, bd=2
        ).pack(pady=10)

        tk.Button(
            button_frame, text="Parar Câmera", command=self.parar_camera, bg="#FF6C63", fg="white",
            font=("Arial", 12, "bold"), relief="raised", padx=25, pady=12, width=18, bd=2
        ).pack(pady=10)

        self.log_label = tk.Label(self, text="Última atividade: Nenhuma", bg="#1e1e1e", fg="white", font=("Arial", 12))
        self.log_label.pack(pady=10)

    def rodar_teste(self):
        print("Rodando teste...")
        self.atualizar_log("Rodando teste...")
        # Chama a função para mover o servo (exemplo: pino 17, ângulo 90)
        move_servo(17, 90)  # Chama a função com parâmetros (pino, ângulo)

    def testar_camera(self):
        print("Testando a câmera...")
        self.atualizar_log("Testando a câmera...")

        self.stop_camera_flag = False
        threading.Thread(target=self._start_camera_stream, daemon=True).start()

    def _start_camera_stream(self):
        start_camera_stream(self.imagem_label, self._stop_camera_flag)

    def parar_camera(self):
        self.stop_camera_flag = True
        self.atualizar_log("Câmera parada.")

    def _stop_camera_flag(self):
        return self.stop_camera_flag

    def atualizar_log(self, mensagem):
        self.log_label.config(text=f"Última atividade: {mensagem}")
