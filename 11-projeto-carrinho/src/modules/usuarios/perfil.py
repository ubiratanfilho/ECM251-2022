from datetime import date


class Perfil():
    def __init__(self, nome) -> None:
        self._nome = nome
        self._foto = ""
        self._data_nascimento = date.today()
        self.descricao = "Sem Descrição"
        self._telefone = "Sem Telefone"
    # Getters e Setters
    def get_nome(self) -> str:
        return self._nome
    def get_foto(self) -> str:
        return self._foto
    def get_data_nascimento(self) -> date:
        return self._data_nascimento
    def get_descricao(self) -> str:
        return self._descricao
    def get_telefone(self) -> str:
        return self._telefone
    def set_nome(self, nome) -> None:
        self._nome = nome
    def set_foto(self, foto) -> None:   
        self._foto = foto
    def set_data_nascimento(self, data_nascimento) -> None: 
        self._data_nascimento = data_nascimento
    def set_descricao(self, descricao) -> None:
        self._descricao = descricao
    def set_telefone(self, telefone) -> None:
        self._telefone = telefone
    