import os
import sys
from typing import Optional, Tuple
from Dominio.Cliente import Cliente
from Repositorio.BDSqlite import BDSqlite
from Repositorio.RepositorioCliente import RepositorioCliente


class Logar:

    def __init__(self):
        conexao = BDSqlite().conectar()
        repositorio = RepositorioCliente(conexao)
        self.repositorio = repositorio

    def executar(self, email: str, senha: str) -> Tuple[bool, str]:
        if not email or not senha:
            return False, "Email e senha são obrigatórios!"
        email_limpo = email.strip().lower()
        registro = self.repositorio.buscarPorEmail(email_limpo)
        if registro is None:
            return False, 'Cliente não encontrado'

        _, nome, email_db, senha_db = registro
        if senha_db != senha:
            return False, 'Senha inválida'

        cliente = Cliente(nome, email_db, senha_db)
        return True, f'Bem-vindo, {cliente.nome()}!'
