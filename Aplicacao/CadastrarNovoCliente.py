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
        # Verificar se o email existe
        buscarUsuario = self.repositorio.buscarPorEmail(email)
        if len(buscarUsuario) > 0 :
            return False, "O email já está em uso"
        if len(senha) < 4:
            return False, "Senha deve ter no mínimo 4 caracteres"
        cliente = Cliente(nome, email, senha)
        if renda is not None:
            cliente.definirRenda(renda)

        cliente_id = self.repositorio.criar(
            cliente.nome(), cliente.email(), cliente.senha()
        )
        return True, f"Cliente cadastrado com sucesso (id={cliente_id})."
