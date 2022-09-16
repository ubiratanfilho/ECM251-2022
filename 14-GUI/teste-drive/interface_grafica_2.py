from tkinter import PhotoImage
from ttkbootstrap.constants import *
import ttkbootstrap as ttk


class MinhaUI(): 
    def _construir_base(self):
        janela = ttk.Window(
            title="Minha GUI Mauá",
            size= (1024, 400),
            position= (100, 100),
            minsize= (600, 300),
            maxsize= (1800, 900),
            alpha=1.0
        )
        janela.iconphoto(False, PhotoImage(file="calculator.png"))
        return janela
    
    def _criar_botao(self, texto, acao):
        # Cria um botão
        bot = ttk.Button(
            self.base,
            text=texto,
            bootstyle=(DEFAULT),
            command=acao,
        )
        bot.pack(side=LEFT, padx=10, pady=5)
        return bot
    
    def _criar_texto(self, guardar):
        return ttk.Entry(
            self.base,
            text=guardar,
            bootstyle=(DEFAULT),
        )
        
    def __init__(self) -> None:
        self.base = self._construir_base()
        self.bot = self._criar_botao("AÇÃO", self.desativar_bot)
        self.bot.grid(row=3, column=2, padx=5, pady=5)
        self.valor_digitado = ""
        self.text = self._criar_texto(guardar=self.valor_digitado)
        self.text.grid(row=2, column=1, padx=5, pady=5)
    def run(self):
        self.base.mainloop()
        
    def mostrar_texto(self):
        print("Valor digitado: ", self.text.get())
        
    def ativar_bot(self):
        print("Ligando o botão")
        self.bot.configure(state="enabled")
    def desativar_bot(self):
        print("Desligando o botão")
        self.bot.configure(state="disabled")
        
if __name__ == "__main__":
    app = MinhaUI()
    app.run()