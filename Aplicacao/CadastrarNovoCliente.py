import os
import sys
from typing import Optional, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from Dominio.Cliente import Cliente
from Repositorio.BDSqlite import BDSqlite
from Repositorio.RepositorioCliente import RepositorioCliente


class CadastrarNovoCliente:

    def __init__(self, repositorio: Optional[RepositorioCliente] = None):
        if repositorio is None:
            conexao = BDSqlite().conectar()
            repositorio = RepositorioCliente(conexao)
        self.repositorio = repositorio

    def executar(self, nome: str, email: str, senha: str, renda: Optional[float] = None) -> Tuple[bool, str]:
        cliente = Cliente(nome, email, senha)
        if renda is not None:
            cliente.definirRenda(renda)

        cliente_id = self.repositorio.criar(
            cliente.nome(), cliente.email(), cliente.senha()
        )
        print(cliente_id)
        return True, f"Cliente cadastrado com sucesso (id={cliente_id})."

cadastrar = CadastrarNovoCliente()
cadastrar.executar('Ramon', 'ramon@agro.com', '1234')