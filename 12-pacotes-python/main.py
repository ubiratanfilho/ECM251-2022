from modelos.documentos import Book, Document, EMail
from modelos.plantas import Arvore, Alface

def run_system():
    doc1 = Document()
    doc2 = EMail(to="Murilao@maua.br", authors=['João', 'Maria'])
    doc3 = Book("Um Ser")
    print(doc3)

if __name__ == '__main__':
    # planta1 = Arvore('Pau-de-laranja')
    # planta2 = Arvore('Pau-de-limão')

    # print(planta1.ola())
    # print(planta2.ola())
    run_system()