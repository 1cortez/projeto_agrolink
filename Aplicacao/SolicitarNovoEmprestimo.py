import os
import sys
from typing import Optional, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from Dominio.Emprestimo import Emprestimo
from Repositorio.BDSqlite import BDSqlite
from Repositorio.RepositorioCliente import RepositorioCliente
from Repositorio.RepositorioEmprestimo import RepositorioEmprestimo


class SolicitarNovoEmprestimo:

    def __init__(
        self,
        repositorio: Optional[RepositorioEmprestimo] = None,
        repositorio_clientes: Optional[RepositorioCliente] = None
    ):
        conexao = None
        if repositorio is None or repositorio_clientes is None:
            conexao = BDSqlite().conectar()

        if repositorio is None:
            repositorio = RepositorioEmprestimo(conexao)
        if repositorio_clientes is None:
            repositorio_clientes = RepositorioCliente(conexao)

        self.repositorio = repositorio
        self.repositorio_clientes = repositorio_clientes

    def executar(self, nome: str, endereco: str, renda, quantia_solicitada, token: Optional[str], classificacao_produtor: str) -> Tuple[bool, str]:
        cliente_id = self._obter_cliente_id_por_token(token)
        if cliente_id is None:
            return False, 'Sessão inválida. Faça login novamente.'

        try:
            renda_normalizada = int(renda)
        except (TypeError, ValueError):
            return False, 'Renda inválida.'

        classificacao_normalizada = (classificacao_produtor or '').strip().lower()

        if classificacao_normalizada == 'pequeno':
            if renda_normalizada >= 500_000:
                return False, 'Renda incompatível para classificação pequeno.'
        elif classificacao_normalizada == 'medio':
            if renda_normalizada < 500_000 or renda_normalizada > 3_000_000:
                return False, 'Renda incompatível para classificação médio.'
        elif classificacao_normalizada == 'grande':
            if renda_normalizada <= 3_000_000:
                return False, 'Renda incompatível para classificação grande.'

        try:
            emprestimo = Emprestimo(
                nome,
                endereco,
                renda_normalizada,
                quantia_solicitada,
                cliente_id,
                classificacao_normalizada or classificacao_produtor
            )
        except ValueError as erro:
            return False, str(erro)

        emprestimo_id = self.repositorio.criar(
            emprestimo.nome(),
            emprestimo.endereco(),
            emprestimo.renda(),
            emprestimo.quantiaSolicitada(),
            emprestimo.clienteId(),
            emprestimo.classificacaoProdutor()
        )
        return True, f"Empréstimo solicitado com sucesso (id={emprestimo_id})."

    def _obter_cliente_id_por_token(self, token: Optional[str]) -> Optional[int]:
        if token is None:
            return None

        token_limpo = token.strip()
        if not token_limpo:
            return None

        registro = self.repositorio_clientes.buscarPorToken(token_limpo)
        if registro is None:
            return None

        try:
            return int(registro[0])
        except (TypeError, ValueError):
            return None
