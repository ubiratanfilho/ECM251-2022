class Item():
    # Construtor
    def __init__(self, nome, preco, descricao=None,imagem=None):
        self._nome = nome
        self._descricao = descricao
        self._preco = preco # _ indica que é privado
        self._imagem = imagem
    
    # Getters
    def get_nome(self):
        return self._nome
    def get_descricao(self):
        return self._descricao
    def get_preco(self):
        return self._preco
    def get_imagem(self):
        return self._imagem
    
    # To String
    def __str__(self):
        return f"{self._nome} - {self._descricao} - {self._preco} - {self._imagem}"
    
    def __eq__(self, __o: object):
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False