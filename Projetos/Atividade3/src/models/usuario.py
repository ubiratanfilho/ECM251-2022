class Usuario():
    def __init__(self, user_name, email, password):
        self._user_name = user_name
        self._email = email
        self._password = password
        
    # Getters e Setters
    def get_user_name(self):
        return self._user_name
    def get_email(self):
        return self._email
    def get_password(self):
        return self._password
    def set_email(self, email):
        self._email = email
    def set_password(self, password):
        self._password = password
    
    def check_password(self, password):
        return self._password == password
    
    def __str__(self):
        return f'{self._user_name} - {self._email} - {self._password}'