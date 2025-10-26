from BDSqlite import BDSqlite

class RepositorioCliente:
    def __init__(self, db):
        self.db = db
    def listarTodos(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

db = BDSqlite().conectar()
cliente = RepositorioCliente(db)
clientes = cliente.listarTodos()
