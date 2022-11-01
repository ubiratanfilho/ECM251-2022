# Ubiratan da Motta Filho
# R.A - 20.00928-3
from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO

class UsuarioController:
    def __init__(self):
        pass
    
    def get_all(self):
        try:
            return UsuarioDAO.get_instance().get_all()
        except:
            raise Exception('Erro ao pegar todos os usuários')
        
    def inserir_usuario(self, usuario):
        try:
            UsuarioDAO.get_instance().inserir_usuario(usuario)
        except:
            raise Exception('Erro ao inserir usuário')
        
    def deletar_usuario(self, usuario):
        try:
            UsuarioDAO.get_instance().deletar_usuario(usuario)
        except:
            raise Exception('Erro ao deletar usuário')
        
    def atualizar_usuario(self, usuario):
        try:
            UsuarioDAO.get_instance().atualizar_usuario(usuario)
        except:
            raise Exception('Erro ao atualizar usuário')
    
    def pegar_usuario(self, user_name):
        try:
            return UsuarioDAO.get_instance().get_usuario(user_name)
        except:
            return None
    
    def limpar_tabela(self):
        try:
            UsuarioDAO.get_instance().limpar_tabela()
        except:
            raise Exception('Erro ao limpar tabela')
        
    def check_login(self, user_name, password):
        try:
            usuario = UsuarioDAO.get_instance().get_usuario(user_name)
            if usuario == None:
                return False
            return usuario.check_password(password)
        except:
            raise Exception('Erro ao checar login')