import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pagina import *

class PaginaInicial(Pagina):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._criar_layout()
        
        
    def _criar_layout(self):
        # barra superior
        barra_superior = ttk.Frame(self, width=1366, height=150, bootstyle="dark")
        barra_superior.pack(fill=X)
        logo = ttk.Label(barra_superior, text="Ubira Tec", font=("Arial"),
                         bootstyle="inverse-dark")
        logo.pack(side=LEFT, padx=20, pady=10)
        carrinho_botao = ttk.Button(barra_superior, text="Carrinho", width=10, bootstyle="secondary")
        carrinho_botao.pack(side=RIGHT, padx=30, pady=10)
        busca = ttk.Entry(barra_superior, width=150)
        busca.pack(side=RIGHT, padx=10, pady=10)
        
        produtos_destaque = ttk.Frame(self, width=1366, height=300, bootstyle="secondary")
        produtos_destaque.pack()
        
if __name__ == "__main__":
    janela = Janela(title="Página Inicial")
    PaginaInicial(janela)
    janela.mainloop()