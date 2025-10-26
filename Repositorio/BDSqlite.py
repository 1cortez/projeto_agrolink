import sqlite3

class BDSqlite:
    def __init__(self):
        self.conexao = sqlite3.connect('dados_usuarios.db')
        self.cursor = self.conexao.cursor()
        self.montarTabelas()
    def conectar(self):
        if self.conexao is None:
            self.conexao = sqlite3.connect('dados_usuarios.db')
        return self.conexao

    def desconectar(self):
        self.conexao.close()
        self.conexao = None

    def montarTabelas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome VARCHAR(30) NOT NULL,
                            email VARCHAR(60) NOT NULL,
                            senha VARCHAR(60) NOT NULL
                            )
                            ''')

        self.conexao.commit()
        self.desconectar()