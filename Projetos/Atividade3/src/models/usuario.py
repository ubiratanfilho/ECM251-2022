class Usuario():
    def __init__(self, user_name, password, email):
        self._user_name = user_name
        self._password = password
        self._email = email
        
    # Getters e Setters
    def get_user_name(self):
        return self._user_name
    def get_email(self):
        return self._email
    def set_email(self, email):
        self._email = email
    def set_password(self, password):
        self._password = password
    
    def check_password(self, password):
        return self._password == password