class Emprestimo:

    CLASSIFICACOES_VALIDAS = ("pequeno", "medio", "grande")

    def __init__(self, nome, endereco, renda, quantia_solicitada, cliente_id, classificacao_produtor, identificador=None):
        self._id = None
        self._nome = ''
        self._endereco = ''
        self._renda = 0
        self._quantia_solicitada = 0
        self._cliente_id = None
        self._classificacao_produtor = ''

        self.definirId(identificador)
        self.definirNome(nome)
        self.definirEndereco(endereco)
        self.definirRenda(renda)
        self.definirQuantiaSolicitada(quantia_solicitada)
        self.definirClienteId(cliente_id)
        self.definirClassificacaoProdutor(classificacao_produtor)

    def id(self):
        return self._id

    def nome(self):
        return self._nome

    def endereco(self):
        return self._endereco

    def renda(self):
        return self._renda

    def quantiaSolicitada(self):
        return self._quantia_solicitada

    def clienteId(self):
        return self._cliente_id

    def classificacaoProdutor(self):
        return self._classificacao_produtor

    def definirId(self, identificador):
        if identificador is None:
            self._id = None
            return

        valor_int = int(identificador)
        if valor_int <= 0:
            raise ValueError('Identificador inválido')

        self._id = valor_int

    def definirNome(self, nome):
        if not nome or not nome.strip():
            raise ValueError('Nome não pode ser vazio')

        nome_limpo = nome.strip().lower()
        self._nome = nome_limpo[:1].upper() + nome_limpo[1:]

    def definirEndereco(self, endereco):
        if not endereco or not endereco.strip():
            raise ValueError('Endereço não pode ser vazio')

        self._endereco = endereco.strip()

    def definirRenda(self, renda):
        renda_int = int(renda)
        if renda_int < 0:
            raise ValueError('Renda não pode ser negativa')

        self._renda = renda_int

    def definirQuantiaSolicitada(self, quantia):
        quantia_int = int(quantia)
        if quantia_int <= 0:
            raise ValueError('Quantia solicitada deve ser positiva')

        self._quantia_solicitada = quantia_int

    def definirClienteId(self, cliente_id):
        cliente_int = int(cliente_id)
        if cliente_int <= 0:
            raise ValueError('Cliente inválido')

        self._cliente_id = cliente_int

    def definirClassificacaoProdutor(self, classificacao):
        if not classificacao or not classificacao.strip():
            raise ValueError('Classificação do produtor é obrigatória')

        normalizado = classificacao.strip().lower()
        if normalizado not in self.CLASSIFICACOES_VALIDAS:
            raise ValueError('Classificação inválida. Utilize pequeno, medio ou grande')

        self._classificacao_produtor = normalizado
