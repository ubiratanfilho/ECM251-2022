import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pagina_inicial import *

class PaginaProduto(PaginaInicial):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
    def _criar_layout(self):
        self._criar_barra_superior()
        self._criar_produto()
        
    def _criar_produto(self):
        pass