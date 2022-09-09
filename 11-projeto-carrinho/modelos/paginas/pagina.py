import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class Pagina(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10)
        self.pack(fill=BOTH, expand=YES)
        
class Janela(ttk.Window):
    def __init__(self, title="Página", **kwargs):
        super().__init__(title=title,
                        size=(1366, 768),
                        **kwargs)
        self.iconphoto(False, PhotoImage(file="../../imagens/Utec.png"))
        
if __name__ == "__main__":
    janela = Janela(title="Página Inicial")
    Pagina(janela)
    janela.mainloop()