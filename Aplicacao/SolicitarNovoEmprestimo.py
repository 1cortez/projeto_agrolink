import os
import sys
from typing import Optional, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from Dominio.Emprestimo import Emprestimo
from Repositorio.BDSqlite import BDSqlite
from Repositorio.RepositorioEmprestimo import RepositorioEmprestimo


class SolicitarNovoEmprestimo:

    def __init__(self, repositorio: Optional[RepositorioEmprestimo] = None):
        if repositorio is None:
            conexao = BDSqlite().conectar()
            repositorio = RepositorioEmprestimo(conexao)
        self.repositorio = repositorio

    def executar(self, nome: str, endereco: str, renda, quantia_solicitada, cliente_id) -> Tuple[bool, str]:
        try:
            emprestimo = Emprestimo(nome, endereco, renda, quantia_solicitada, cliente_id)
        except ValueError as erro:
            return False, str(erro)

        emprestimo_id = self.repositorio.criar(
            emprestimo.nome(),
            emprestimo.endereco(),
            emprestimo.renda(),
            emprestimo.quantiaSolicitada(),
            emprestimo.clienteId()
        )
        return True, f"Empréstimo solicitado com sucesso (id={emprestimo_id})."
