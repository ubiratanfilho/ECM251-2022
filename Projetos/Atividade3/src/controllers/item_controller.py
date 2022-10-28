# Ubiratan da Motta Filho
# R.A - 20.00928-3
from models.item import Item
from dao.item_dao import ItemDAO

class ItemController:
    def __init__(self):
        pass
    
    def get_all(self):
        try:
            return ItemDAO.get_instance().get_all()
        except:
            return False
    
    def inserir_item(self, item):
        try:
            ItemDAO.get_instance().inserir_item(item)
            return True
        except:
            return False
        
    def deletar_item(self, item):
        try:
            ItemDAO.get_instance().deletar_item(item)
            return True
        except:
            return False
    
    def atualizar_item(self, item):
        try:
            ItemDAO.get_instance().atualizar_item(item)
            return True
        except:
            return False
    
    def pegar_item(self, id):
        try:
            return ItemDAO.get_instance().pegar_item(id)
        except:
            return False
        
    def limpar_tabela(self):
        try:
            ItemDAO.get_instance().limpar_tabela()
            return True
        except:
            return False