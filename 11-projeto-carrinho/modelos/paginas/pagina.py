import ttkbootstrap as ttk

class Pagina():
    def _construir_base(self):
        janela = ttk.Window(
            title="Página",
            size=(1440, 1024),
        )
        return janela
    
    def __init__(self) -> None:
        self.base = self._construir_base()
        
    def run(self):
        self.base.mainloop()
        
if __name__ == "__main__":
    app = Pagina()
    app.run()