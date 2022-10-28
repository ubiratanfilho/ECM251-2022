from models.usuario import Usuario
import sqlite3

class UsuarioDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()
        
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UsuarioDAO()
        return cls._instance
    
    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')
        
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Usuarios;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Usuario(user_name=resultado[0], 
                                   email=resultado[1], 
                                   password=resultado[2]))
        self.cursor.close()
        return resultados

    def inserir_usuario(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Usuarios (usuario, email, senha)
            VALUES(?,?,?);
        """, (usuario.get_user_name(), usuario.get_email(), usuario.get_password()))
        self.conn.commit()
        self.cursor.close()
        
    def deletar_usuario(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Usuarios WHERE usuario = ?;
        """, (usuario.get_user_name(),))
        self.conn.commit()
        self.cursor.close()
    
    def atualizar_usuario(self, usuario):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            UPDATE Usuarios SET email = ?, senha = ? WHERE usuario = ?;
        """, (usuario.get_email(), usuario.get_password(), usuario.get_user_name()))
        self.conn.commit()
        self.cursor.close()
        
    def get_usuario(self, user_name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Usuarios WHERE usuario = ?;
        """, (user_name,))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return Usuario(user_name=resultado[0], 
                       email=resultado[1], 
                       password=resultado[2])
        
    def limpar_tabela(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Usuarios;
        """)
        self.conn.commit()
        self.cursor.close()