from tkinter import PhotoImage
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class Cards():
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
    
    def __init__(self) -> None:
        self.base = self._construir_base()
        self.bot = self._criar_botao("AÇÃO", self.desativar_bot)
        self.bot.grid(row=3, column=2, padx=5, pady=5)
        self.valor_digitado = ""
        self.text = self._criar_texto(guardar=self.valor_digitado)
        self.text.grid(row=2, column=1, padx=5, pady=5)
    def run(self):
        self.base.mainloop()
        
if __name__ == "__main__":
    app = Cards()
    app.run()