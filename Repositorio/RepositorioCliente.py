from .BDSqlite import BDSqlite

class RepositorioCliente:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, email, senha):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )
        self.db.commit()
        return cursor.lastrowid

    def listarTodos(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

    def buscarPorId(self, cliente_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
        return cursor.fetchone()

    def atualizar(self, cliente_id, nome, email, senha):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE clientes SET nome = ?, email = ?, senha = ? WHERE id = ?",
            (nome, email, senha, cliente_id)
        )
        self.db.commit()
        return cursor.rowcount

    def deletar(self, cliente_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        self.db.commit()
        return cursor.rowcount
