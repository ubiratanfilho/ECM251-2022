import ttkbootstrap as ttk
from pagina import Pagina

class PaginaInicial(Pagina):
    def _construir_base(self):
        janela = ttk.Window(
            title="Página Inicial",
            size=(1440, 1024),
        )
        return janela
    
    
if __name__ == "__main__":
    app = PaginaInicial()
    app.run()