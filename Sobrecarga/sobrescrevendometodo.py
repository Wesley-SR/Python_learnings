# =============================================================================
# CLASS'S
# =============================================================================

class Pessoa():

    def __init__(self, nome, idade, sexo):

        self._nome = nome
        self._idade = idade
        self._sexo = sexo

        self._check()

    def _check(self):

        if isinstance(self._nome, str) == False:
            message = f"O nome deve possuir retorno {type(str())}"
            raise ValueError(message)

        elif isinstance(self._idade, int) == False:
            message = f"A idade deve possuir retorno {type(int())}"
            raise ValueError(message)

        elif isinstance(self._sexo, str) == False:
            message = f"O sexo deve possuir retorno {type(str())}"
            raise ValueError(message)

        elif self._sexo not in ["M","F"]:
            message = f"O sexo deve ser passado na forma como: (M) masculino ou (F) feminino"
            raise ValueError(message)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    def fazerAniversario(self):
        self._idade += 1

    def __str__(self):
        CABECALHO = "\n***********************************\n"
        NOME = f"\n\nNOME: {self._nome}"
        IDADE = f"\nIDADE: {self._idade} ano(s)"
        if(self._sexo == "M"):
            SEXO = f"\nSEXO: ({self._sexo}) - masculino"
        else:
            SEXO = f"\nSEXO: ({self._sexo}) - feminino"
        message = CABECALHO + f"DADOS - PESSOA:" + NOME + IDADE + SEXO + CABECALHO
        return message

class Aluno(Pessoa):

    def __init__(self,matricula, curso, **kwargs):
        super().__init__(**kwargs)
        self._matricula = matricula
        self._curso = curso

        self._check_aluno()

    def _check_aluno(self):

        if isinstance(self._matricula, str) == False:
            message = f"A matrícula deve possuir retorno {type(str())}"
            raise ValueError(message)

        elif isinstance(self._curso, str) == False:
            message = f"O curso deve possuir retorno {type(str())}"
            raise ValueError(message)

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def sexo(self, matricula):
        self._matricula = matricula

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    def pagarMensalidade(self):
        nome = self.nome
        message = f"Pagando mensalidade do aluno: {nome}"
        print(message)

    def __str__(self):
        CABECALHO = "\n***********************************\n"
        NOME = f"\n\nNOME: {self._nome}"
        IDADE = f"\nIDADE: {self._idade} ano(s)"
        if(self._sexo == "M"):
            SEXO = f"\nSEXO: ({self._sexo}) - masculino"
        else:
            SEXO = f"\nSEXO: ({self._sexo}) - feminino"
        CURSO = f"\nCURSO: {self._curso}"
        MATRICULA = f"\nMATRÍCULA: {self._matricula}"
        message = CABECALHO + f"DADOS - ALUNO:" + NOME + IDADE + SEXO + MATRICULA + CURSO + CABECALHO
        return message

class Bolsista(Aluno):

    def __init__(self, bolsa, **kwargs):
        super().__init__(**kwargs)
        self._bolsa = bolsa

    def _check_bolsista(self):

        if isinstance(self._bolsa, float) == False:
            message = f"O valor da bolsa deve possuir retorno {type(float())}"
            raise ValueError(message)

    def renovarBolsa(self):
        print(f"Renovando bolsa de {self._nome}")

    def pagarMensalidade(self):
        print(f"{self._nome} é bolsista! Pagamento facilitado")

    @property
    def bolsa(self):
        return self._bolsa

    @bolsa.setter
    def bolsa(self, bolsa):
        self._bolsa = bolsa

    def __str__(self):
        CABECALHO = "\n***********************************\n"
        NOME = f"\n\nNOME: {self._nome}"
        IDADE = f"\nIDADE: {self._idade} ano(s)"
        if(self._sexo == "M"):
            SEXO = f"\nSEXO: ({self._sexo}) - masculino"
        else:
            SEXO = f"\nSEXO: ({self._sexo}) - feminino"
        CURSO = f"\nCURSO: {self._curso}"
        MATRICULA = f"\nMATRÍCULA: {self._matricula}"
        BOLSA = f"\nVALOR BOLSA: R$ {self._bolsa}"
        message = CABECALHO + f"DADOS - ALUNO:" + NOME + IDADE + SEXO + MATRICULA + CURSO + BOLSA + CABECALHO
        return message

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":

    bolsista = Bolsista(12.5, matricula="1612130075", curso="CCO", nome="Fulano", idade=21, sexo="M")

    print(bolsista)

    bolsista.pagarMensalidade()