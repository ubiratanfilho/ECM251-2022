import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pagina import *
from pagina_inicial import *

class PaginaCarrinho(PaginaInicial):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    
    def _criar_layout(self):
        self._criar_barra_superior()
        self._criar_carrinho()
        
    def _criar_carrinho(self):
        bloco = ttk.Frame(self, bootstyle="secondary", width=1000, height=1000)
        bloco.pack(pady=20, fill=Y)

if __name__ == "__main__":
    janela = Janela(title="Carrinho")
    PaginaCarrinho(janela)
    janela.mainloop()        