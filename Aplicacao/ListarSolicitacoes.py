import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from Repositorio.BDSqlite import BDSqlite
from Repositorio.RepositorioCliente import RepositorioCliente
from Repositorio.RepositorioEmprestimo import RepositorioEmprestimo


class ListarSolicitacoes:

    def __init__(self, repositorio=None, repositorio_clientes=None):
        conexao = None
        if repositorio is None or repositorio_clientes is None:
            conexao = BDSqlite().conectar()

        if repositorio is None:
            repositorio = RepositorioEmprestimo(conexao)
        if repositorio_clientes is None:
            repositorio_clientes = RepositorioCliente(conexao)

        self.repositorio = repositorio
        self.repositorio_clientes = repositorio_clientes

    def executar(self, token):
        if token is None:
            return False, 'Sessão inválida. Faça login novamente.', []

        token_limpo = token.strip()
        if not token_limpo:
            return False, 'Sessão inválida. Faça login novamente.', []

        cliente = self.repositorio_clientes.buscarPorToken(token_limpo)
        if cliente is None:
            return False, 'Sessão inválida. Faça login novamente.', []

        cliente_id = cliente[0]
        emprestimos = self.repositorio.listarPorCliente(cliente_id)
        return True, 'Solicitações carregadas com sucesso.', emprestimos
