import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pagina import *

class PaginaLogin(Pagina):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self._criar_layout()
        
    def _criar_layout(self):
        self._criar_caixa_login()
        
    def _criar_caixa_login(self):
        caixa_login = ttk.Frame(self, width=500, height=500, bootstyle="secondary")
        caixa_login.pack(pady=200)
        titulo = ttk.Label(caixa_login, text="Login", bootstyle="inverse-secondary",
                           font=("Arial", 20))
        titulo.pack(pady=10)
        
        usuario_box = ttk.Frame(caixa_login, width=500, height=100, bootstyle="secondary")
        usuario_box.pack(pady=10)
        usuario_label = ttk.Label(usuario_box, text="Usuário", bootstyle="inverse-secondary")
        usuario_label.pack(side=LEFT, padx=10)
        usuario_entry = ttk.Entry(usuario_box, width=30)
        usuario_entry.pack(side=LEFT, padx=10)
        
        senha_box = ttk.Frame(caixa_login, width=500, height=100, bootstyle="secondary")
        senha_box.pack(pady=10)
        senha_label = ttk.Label(senha_box, text="Senha  ", bootstyle="inverse-secondary")
        senha_label.pack(side=LEFT, padx=10)
        senha_entry = ttk.Entry(senha_box, width=30)
        senha_entry.pack(side=LEFT, padx=10)
    

if __name__ == "__main__":
    janela = Janela(title="Login")
    PaginaLogin(janela)
    janela.mainloop()