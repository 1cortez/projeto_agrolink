import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "dados_usuarios.db"

class BDSqlite:
    def __init__(self):
        self.caminho_bd = Path(DB_PATH)
        self.conexao = sqlite3.connect(self.caminho_bd)
        self.cursor = self.conexao.cursor()
        self.montarTabelas()
    def conectar(self):
        if self.conexao is None:
            self.conexao = sqlite3.connect(self.caminho_bd)
        return self.conexao

    def desconectar(self):
        self.conexao.close()
        self.conexao = None

    def montarTabelas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome VARCHAR(30) NOT NULL,
                            email VARCHAR(60) NOT NULL,
                            senha VARCHAR(60) NOT NULL,
                            token TEXT
                            )
                            ''')

        self.conexao.commit()
        self.desconectar()
