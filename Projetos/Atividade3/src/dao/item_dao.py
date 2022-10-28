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
                                   imagem=resultado[4],
                                   id=resultado[0]))
        self.cursor.close()
        return resultados
    
    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Produtos (nome, descricao, preco, imagem)
            VALUES(?,?,?,?);
        """, (item.get_nome(), item.get_descricao(), item.get_preco(), item.get_imagem()))
        self.conn.commit()
        item.set_id(self.cursor.lastrowid)
        self.cursor.close()
        
    def deletar_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Produtos WHERE id = ?;
        """, (item.get_id(),))
        self.conn.commit()
        self.cursor.close()
        
    def atualizar_item(self, item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Produtos SET nome = ?, descricao = ?, preco = ?, imagem = ? WHERE id = ?;
            """, (item.get_nome(), item.get_descricao(), item.get_preco(), item.get_imagem(), item.get_id()))
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def pegar_item(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Produtos WHERE id = ?;
        """, (id,))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        return Item(nome=resultado[1], 
                    descricao=resultado[2], 
                    preco=resultado[3], 
                    imagem=resultado[4],
                    id=resultado[0])    
    
    def limpar_tabela(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            DELETE FROM Produtos;
        """)
        self.cursor.execute("""
            DELETE FROM sqlite_sequence WHERE name = 'Produtos';
        """)
        self.conn.commit()
        self.cursor.close()
    