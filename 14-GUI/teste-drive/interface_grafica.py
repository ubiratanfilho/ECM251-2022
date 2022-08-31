from tkinter import PhotoImage
from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class MinhaUI():
    def acao_botao(self):
        print("Click!")
        
    def _construir_base(self):
        janela = ttk.Window(
            title="Minha GUI Mauá",
            size= (1024, 400),
            position= (100, 100),
            minsize= (600, 300),
            maxsize= (1800, 900),
            alpha=0.75
        )
        janela.iconphoto(False, PhotoImage(file="calculator.png"))
        return janela
        
    def __init__(self) -> None:
        self.base = self._construir_base()
        
        # Criando um botão
        ttk.Button(
            self.base,
            text="Olá Mundo",
            bootstyle="default",
            command=self.ativar_bot,
        ).pack(side=LEFT, padx=10, pady=5)

        # Criando um segundo botão
        bot2 = ttk.Button(
            self.base,
            text="Segundo Botão",
            bootstyle=(DANGER, OUTLINE),
            command=self.desativar_bot,
        )
        bot2.pack(side=LEFT, padx=10, pady=5)
        
    def run(self):
        self.base.mainloop()
        
    def ativar_bot(self):
        print("Ligando o botão")
        self.bot2.configure(state="enabled")
    def desativar_bot(self):
        print("Desligando o botão")
        self.bot2.configure(state="disabled")
        
if __name__ == "__main__":
    app = MinhaUI()
    app.run()