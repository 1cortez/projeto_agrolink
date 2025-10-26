class Cliente:

    def __init__(self, nome, email, senha):
        self._nome = ''
        self._email = ''
        self._senha = ''
        self._renda = 0.0

        self.definirNome(nome)
        self.definirEmail(email)
        self.definirSenha(senha)

    def nome(self):
        return self._nome

    def email(self):
        return self._email

    def senha(self):
        return self._senha

    def renda(self):
        return self._renda

    def definirNome(self, nome: str):
        if not nome or not nome.strip():
            raise ValueError('Nome não pode ser vazio')

        nome_limpo = nome.strip()
        self._nome = nome_limpo[:1].upper() + nome_limpo[1:]

    def definirEmail(self, email: str):
        if not email:
            raise ValueError('Email não pode ser vazio')

        email_limpo = email.strip().lower()

        if not '@' in email_limpo:
            raise ValueError('Email inválido')

        self._email = email_limpo

    def definirSenha(self, senha: str):
        if not senha:
            raise ValueError('Senha não pode ser vazia')

        self._senha = senha

    def definirRenda(self, renda: float):
        renda_float = float(renda)

        if renda_float < 0:
            raise ValueError('Renda não pode ser negativa')

        self._renda = renda_float
