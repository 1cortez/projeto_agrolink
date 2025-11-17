class RepositorioEmprestimo:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, endereco, renda):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO emprestimo (nome, endereco, renda) VALUES (?, ?, ?)",
            (nome, endereco, renda)
        )
        self.db.commit()
        return cursor.lastrowid

    def listarTodos(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM emprestimo")
        return cursor.fetchall()

    def buscarPorId(self, emprestimo_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM emprestimo WHERE id = ?", (emprestimo_id,))
        return cursor.fetchone()

    def atualizar(self, emprestimo_id, nome, endereco, renda):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE emprestimo SET nome = ?, endereco = ?, renda = ? WHERE id = ?",
            (nome, endereco, renda, emprestimo_id)
        )
        self.db.commit()
        return cursor.rowcount

    def deletar(self, emprestimo_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM emprestimo WHERE id = ?", (emprestimo_id,))
        self.db.commit()
        return cursor.rowcount
