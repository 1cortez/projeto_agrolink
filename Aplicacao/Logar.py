import os
import sys
import secrets
from typing import Optional, Tuple
from Dominio.Cliente import Cliente
from Repositorio.BDSqlite import BDSqlite
from Repositorio.RepositorioCliente import RepositorioCliente
import bcrypt

class Logar:

    def __init__(self):
        conexao = BDSqlite().conectar()
        repositorio = RepositorioCliente(conexao)
        self.repositorio = repositorio

    def executar(self, email: str, senha: str) -> Tuple[bool, str, Optional[int], Optional[str]]:
        if not email or not senha:
            return False, "Email e senha são obrigatórios!", None, None
        email_limpo = email.strip().lower()
        registro = self.repositorio.buscarPorEmail(email_limpo)
        if registro is None:
            return False, 'Cliente não encontrado', None, None

        cliente_id, nome, email_db, senha_db, _ = registro

        if not bcrypt.checkpw(senha.encode(), senha_db.encode()):
            return False, 'Senha inválida', None, None

        token = self._gerar_token()
        self.repositorio.atualizarToken(cliente_id, token)

        cliente = Cliente(nome, email_db, senha_db)
        return True, f'Bem-vindo, {cliente.nome()}!', cliente_id, token

    def buscar_cliente_por_token(self, token: Optional[str]):
        if not token:
            return None
        return self.repositorio.buscarPorToken(token)

    def encerrar_sessao(self, token: Optional[str]):
        if not token:
            return
        self.repositorio.limparTokenPorValor(token)

    def _gerar_token(self) -> str:
        return secrets.token_hex(32)
