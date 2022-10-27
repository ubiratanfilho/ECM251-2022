from dao.item_dao import ItemDAO
from models.item import Item

# Adicionar item
item = Item(20.99, "Ubiratec Start", "Primeiro Produto Ubiratec", "https")
ItemDAO.get_instance().inserir_item(item)

all_items = ItemDAO.get_instance().get_all()
for i in all_items:
    print(i)