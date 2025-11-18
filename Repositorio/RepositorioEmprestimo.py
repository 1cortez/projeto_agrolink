class RepositorioEmprestimo:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, endereco, renda, quantia_solicitada):
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO emprestimos (nome, endereco, renda, quantia_solicitada) VALUES (?, ?, ?, ?)",
            (nome, endereco, renda, quantia_solicitada)
        )
        self.db.commit()
        return cursor.lastrowid

    def listarTodos(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM emprestimos")
        return cursor.fetchall()

    def buscarPorId(self, emprestimo_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM emprestimos WHERE id = ?", (emprestimo_id,))
        return cursor.fetchone()

    def atualizar(self, emprestimo_id, nome, endereco, renda, quantia_solicitada):
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE emprestimos SET nome = ?, endereco = ?, renda = ?, quantia_solicitada = ? WHERE id = ?",
            (nome, endereco, renda, quantia_solicitada, emprestimo_id)
        )
        self.db.commit()
        return cursor.rowcount

    def deletar(self, emprestimo_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM emprestimos WHERE id = ?", (emprestimo_id,))
        self.db.commit()
        return cursor.rowcount
