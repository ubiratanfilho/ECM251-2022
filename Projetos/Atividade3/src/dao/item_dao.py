import sqlite3
from models.item import Item

class ItemDAO:
    _instance = None
    
    def __init__(self) -> None:
        self._connect()
        
    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ItemDAO()
        return cls._instance
    
    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')
        
    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Produtos;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Item(nome=resultado[1], 
                                   descricao=resultado[2], 
                                   preco=resultado[3], 
                                   imagem=resultado[4]))
        self.cursor.close()
        return resultados
    
    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Produtos (nome, descricao, preco, imagem)
            VALUES(?,?,?,?);
        """, (item.get_nome(), item.get_descricao(), item.get_preco(), item.get_imagem()))
        self.conn.commit()
        self.cursor.close()
        
    def deletar_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Produtos WHERE nome = ?;
        """, (item.get_nome(),))
        self.conn.commit()
        self.cursor.close()
        
    def atualizar_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Produtos SET nome = ?, descricao = ?, preco = ?, imagem = ? WHERE nome = ?;
            """, (item.get_nome(), item.get_descricao(), item.get_preco(), item.get_imagem(), item.get_nome()))
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def limpar_tabela(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Produtos;
        """)
        self.conn.commit()
        self.cursor.close()