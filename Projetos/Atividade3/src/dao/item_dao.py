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
            resultados.append(Item(resultado[1], resultado[2], resultado[3], resultado[4]))
        self.cursor.close()
        return resultados
    
    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Produtos (id, preco, nome, descricao, imagem)
            VALUES(?,?,?,?,?);
        """, (item.get_id(), item.get_preco(), item.get_nome(), item.get_descricao(), item.get_imagem()))
        self.conn.commit()
        self.cursor.close()