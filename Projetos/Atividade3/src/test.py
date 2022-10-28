from dao.item_dao import ItemDAO
from models.item import Item
from controllers.item_controller import ItemController

# Criação de itens
p1 = Item("UbiraTec Washer", "Lavadora de tênis e sapatos", 354.99, "./imagens/washer.png")
p2 = Item("Samsung Neo G9", "Monitor Gamer Samsung Curvado", 9999.99, "./imagens/neog9.jfif")
p3 = Item("Nike PG4 Gatorade", "Tênis de Basquete do Paul George", 449.99, "./imagens/pg4.png")

# Adicionando itens ao banco de dados
controller = ItemController()
controller.inserir_item(p1)
controller.inserir_item(p2)
controller.inserir_item(p3)

# Pegando todos os itens do banco de dados
for item in controller.get_all():
    print(item)
print()

# Deletando um item do banco de dados
controller.deletar_item(p2)

# Atualizando um item do banco de dados
p2.set_nome("Samsung Neo G9 2.0")
p2.set_descricao("Monitor Gamer Samsung Curvado 2.0")
p2.set_preco(10999.99)
p2.set_imagem("./imagens/neog9_2.0.jfif")
controller.atualizar_item(p2)

# Exibindo todos os itens do banco de dados
for item in controller.get_all():
    print(item)

# Limpar a tabela
controller.limpar_tabela()