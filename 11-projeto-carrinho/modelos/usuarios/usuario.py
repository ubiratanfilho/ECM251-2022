from modelos.usuarios.perfil import Perfil


class Usuario():
    def __init__(self, user_name, password, email) -> None:
        self._user_name = user_name
        self._password = password
        self._email = email
        self._perfil = Perfil(nome=user_name)
        
    def get_user_name(self) -> str:
        return self._user_name
    def get_perfil(self) -> Perfil:
        return self._perfil
    
    def check_password(self, password) -> bool:
        return self._password == password