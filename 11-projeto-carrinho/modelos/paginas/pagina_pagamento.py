import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pagina_inicial import *

class PaginaPagamento(PaginaInicial):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    def _criar_layout(self):
        self._criar_barra_superior()
        self._criar_pagamento()
    
    def _criar_pagamento(self):
        pass
        
if __name__ == "__main__":
    janela = Janela(title="Pagamento")
    PaginaPagamento(janela)
    janela.mainloop()