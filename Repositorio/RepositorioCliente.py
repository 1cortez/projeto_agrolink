import bcrypt

class RepositorioCliente:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, email, senha):
        cursor = self.db.cursor()
        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        senha_hash = senha_hash.decode()
        cursor.execute(
            "INSERT INTO clientes (nome, email, senha, token) VALUES (?, ?, ?, ?)",
            (nome, email, senha_hash, None)
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

    def buscarPorEmail(self, email):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clientes WHERE email = ?", (email,))
        return cursor.fetchone()

    def buscarPorToken(self, token):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clientes WHERE token = ?", (token,))
        return cursor.fetchone()

    def atualizar(self, cliente_id, nome, email, senha):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE clientes SET nome = ?, email = ?, senha = ? WHERE id = ?",
            (nome, email, senha, cliente_id)
        )
        self.db.commit()
        return cursor.rowcount

    def atualizarToken(self, cliente_id, token):
        cursor = self.db.cursor()
        cursor.execute("UPDATE clientes SET token = ? WHERE id = ?", (token, cliente_id))
        self.db.commit()
        return cursor.rowcount

    def limparTokenPorValor(self, token):
        cursor = self.db.cursor()
        cursor.execute("UPDATE clientes SET token = NULL WHERE token = ?", (token,))
        self.db.commit()
        return cursor.rowcount

    def deletar(self, cliente_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        self.db.commit()
        return cursor.rowcount
