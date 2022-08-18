class Item():
    # Construtor
    def __init__(self, preco, nome, descricao=None):
        self._preco = preco # _ indica que é privado
        self._nome = nome
        self._descricao = descricao
    
    # Getters
    def get_nome(self):
        return self._nome
    def get_preco(self):
        return self._preco
    def get_descricao(self):
        return self._descricao
    
    # To String
    def __str__(self):
        return f"{self._nome} - {self._preco} - {self._descricao}"
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Item):
            return self._nome == __o.get_nome()
        return False