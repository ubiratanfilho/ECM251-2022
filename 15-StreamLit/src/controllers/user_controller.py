from models.user import User

class UserController():
    def __init__(self) -> None:
        # Carrega os dados dos usuários
        self.users = [
            User(name="admin", password="admin", email="oi@gmail.com"),
            User(name="admin2", password="admin2", email="oi"),
            User(name="admin3", password="admin3", email="oi"),
        ]
    def checkUser(self, user):
        return user in self.users
    
    def checkLogin(self, name, password):
        for user in self.users:
            if user.name == name and user.password == password:
                return True
        return False