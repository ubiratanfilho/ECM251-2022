class Item():
    # Construtor
    def __init__(self, nome, descricao, preco,imagem=None, id=None):
        self._nome = nome
        self._descricao = descricao
        self._preco = preco # _ indica que é privado
        self._imagem = imagem
        self._id = id
    
    # Getters e Setters
    def get_nome(self):
        return self._nome
    def get_descricao(self):
        return self._descricao
    def get_preco(self):
        return self._preco
    def get_imagem(self):
        return self._imagem
    def get_id(self):
        return self._id
    def set_nome(self, nome):
        self._nome = nome
    def set_descricao(self, descricao):
        self._descricao = descricao
    def set_preco(self, preco): 
        self._preco = preco
    def set_imagem(self, imagem):
        self._imagem = imagem
    def set_id(self, id):
        self._id = id
    
    def __str__(self):
        return f"{self._id} - {self._nome} - {self._descricao} - {self._preco} - {self._imagem}"
    
    def __eq__(self, __o: object):
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False