import tkinter as tk
from tkinter import Button, Label, Entry

class Login(tk.Frame):
    def __init__(self, master, router, **kwargs):  # Adicionando 'router' como argumento
        super().__init__(master, bg="#333333", **kwargs)
        self.router = router  # Armazenando o router

        # Container centralizado para login com bordas arredondadas
        self.container = tk.Frame(self, bg="#444444", padx=40, pady=40, bd=5, relief="solid", borderwidth=2)
        self.container.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o container na tela

        # Título do Login
        Label(self.container, text="Bem-vindo ao NicoCam", bg="#444444", fg="white", font=("Arial", 20, "bold")).pack(pady=20)

        # Campo para o nome de usuário
        self.usuario_label = Label(self.container, text="Usuário", bg="#444444", fg="white", font=("Arial", 12))
        self.usuario_label.pack(pady=(10, 5))
        self.usuario_entry = Entry(self.container, bg="#555555", fg="white", font=("Arial", 14), bd=0, relief="solid",
                                   insertbackground="white", justify="center")
        self.usuario_entry.pack(pady=5, ipadx=10, ipady=5, fill="x")
        self.usuario_entry.focus()

        # Campo para a senha
        self.senha_label = Label(self.container, text="Senha", bg="#444444", fg="white", font=("Arial", 12))
        self.senha_label.pack(pady=(10, 5))
        self.senha_entry = Entry(self.container, bg="#555555", fg="white", font=("Arial", 14), bd=0, relief="solid",
                                 insertbackground="white", justify="center", show="*")
        self.senha_entry.pack(pady=5, ipadx=10, ipady=5, fill="x")

        # Botão de login com sombra e borda arredondada
        login_button = Button(self.container, text="Entrar", command=self.fazer_login, bg="#6C63FF", fg="white",
                              font=("Arial", 14, "bold"), relief="flat", padx=10, pady=10, width=15)
        login_button.pack(pady=20)

        # Efeito de sombra no botão (adicionando uma cor de fundo mais escura no hover)
        login_button.bind("<Enter>", lambda e: login_button.config(bg="#5A4CCC"))
        login_button.bind("<Leave>", lambda e: login_button.config(bg="#6C63FF"))

        # Link de "Esqueci minha senha"
        self.recuperar_senha = Label(self.container, text="Esqueci minha senha", bg="#444444", fg="#6C63FF",
                                     font=("Arial", 10, "underline"), cursor="hand2")
        self.recuperar_senha.pack(pady=(10, 0))

        self.pack(fill="both", expand=True)  # Garantir que o frame ocupe todo o espaço disponível

    def fazer_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        # Aqui você pode fazer a verificação de login com o backend ou lógica que você preferir
        if usuario == "admin" and senha == "1234":  # Exemplo simples de verificação
            print("Login bem-sucedido!")
            self.router.navigate_to("Home")  # Navega para a próxima página
        else:
            print("Usuário ou senha inválidos!")
            # Exibindo uma mensagem de erro simples
            self.usuario_entry.delete(0, tk.END)
            self.senha_entry.delete(0, tk.END)
            self.usuario_entry.focus()
