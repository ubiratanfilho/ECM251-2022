import ttkbootstrap as ttk
from pagina import Pagina

class PaginaInicial(Pagina):
    def _construir_base(self):
        janela = ttk.Window(
            title="Página Inicial",
            size=(1366, 768),
        )
        
        # Adicionando frames
        ttk.Frame(
            janela,
            bootstyle="dark",
            width=1366,
            height=100,
        ).pack()
        
        ttk.Frame(
            janela,
            bootstyle="secondary",
            width=1366,
            height=300,
        ).pack()
        
        return janela
    
    
if __name__ == "__main__":
    app = PaginaInicial()
    app.run()