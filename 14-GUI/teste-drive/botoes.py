from tkinter import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

base = ttk.Window(
    title="Minha GUI Mauá",
    size= (1024, 400),
    position= (100, 100),
    minsize= (600, 300),
    maxsize= (1800, 900),
    alpha=0.75
)
base.iconphoto(False, PhotoImage(file="calculator.png"))

def acao_botao():
    print("Click!")

# Criando um botão
ttk.Button(
    base,
    text="Olá Mundo",
    bootstyle="default",
    command=acao_botao,
).pack(side=LEFT, padx=10, pady=5)

# Ponto de entrada da interface
base.mainloop()