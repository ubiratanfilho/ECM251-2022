class Conta:
    def __init__(self, id=None, historico= []) -> None:
        self._id = id
        self._historico = historico
    def get_historico(self) -> list:
        return self._historico
    