'''
Referências:
1) https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python
2) https://www.youtube.com/watch?v=oOAmgnFFqbQ
3) 
Uma função declarada como __nome_funcao(): só pode ser acessada
de dentro da classe que ela foi definida. Se essa função for de-
clarada na função pai(), uma subclasse não tem acesso a função.
Apenas detro da classe declarada mesmo.

Se a função for declarada _nome_funcao():, apenas indica que não
é para mexer, mas da para alterar de fora da função.

Na verdade declarar _nome_função(): e nome_função(): da na mesma
em termos de código e acesso, mas com um "_" indica ao programador
que não é para mexer e não necessáriamente bloqueia o acesso.

O mesmo ocorre para variáveis...


O "self." é o que permite que os métodos da classe utilize a variável
Se tenho vários objetos da minha classe, o "self." que distingue de qual
objeto está se referindo no momento.
'''
class Fachada():
    def __init__(self, objeto_entrada):
        self.__objeto_entrada = objeto_entrada
    
    def teste_achar_nome(self):
        self.__objeto_entrada.teste()

class Pessoa():
    def __init__(self, nome, idade):
        self.__idade = idade
        self.nome_pessoa = nome
        self.comida_favorita = 'Costela assada'
        # Um método que herda a classe "Pessoa" tem acesso a comida favorita
        self.__bebida_favorita = 'Agua'
        # Apenas um método interno da classe "Pessoa" tem acesso a bebida favorita
        print('Construindo a classe Mae')
        print('O nome da mae é  ', nome)
        print('A idade da mae é ', self.__idade)
        self.seleciona_geracao()
        print('Era para ter dito a gerecao ')

    def diz_bebida_favorita(self):
        print('Minha bebida favorita é ', self.__bebida_favorita)

    def seleciona_geracao(self):
        print("Entlou")
        if (self.__idade == 15):
            print("Geracao coca cola")

    def teste(self):
        pass

class Homem(Pessoa):
    def __init__(self, nome, idade, canivete):
        super().__init__(nome, idade)
        self.__cabelo_da_namorada = 'Castanho escuro'
        # Apenas um método interno pode acessar o cabelo da namorada
        print('Marca do canivete:  ', canivete)

    def altera_nome(self, novo_nome):
        print('\nAlterando nome\n')
        self.nome_pessoa = novo_nome

    def imprime_nome(self):
        print('Nome = ', self.nome_pessoa)

    def __funcao_privada(self):
        print('Sou privada')

    def acessa_funcao(self):
        self.__funcao_privada()
    
    def pinta_cabelo_da_namorada(self, nova_cor):
        self.__cabelo_da_namorada = nova_cor
    
    def diz_cor_cabelo(self):
        print(self.__cabelo_da_namorada)

    def diz_comida_favorita(self):
        print('A minha comida favorita é', self.comida_favorita)
    
    def teste(self):
        print("Eu sou uma subscricao\n")


nome_pessoa = 'Wesley'
idade_pessoa = 15
marca_canivete = 'Victor Inox'

wesley = Homem(nome_pessoa, idade_pessoa, marca_canivete)

wesley.imprime_nome()
wesley.altera_nome('Ana')
wesley.imprime_nome()

wesley.acessa_funcao() # A função "acessa_funcao" tem acesso a função "__funcao_privada"
#wesley.__funcao_privada() # Não consigo acessar

wesley.diz_cor_cabelo()
wesley.pinta_cabelo_da_namorada('Loiro')
wesley.diz_cor_cabelo()

wesley.diz_comida_favorita()
wesley.diz_bebida_favorita()
wesley.__nome_pessoa = 'Amanda' # Quando não tem restrição,
# é possível alterar de fora da classe
wesley.imprime_nome()


wesley = Homem(nome_pessoa, idade_pessoa, marca_canivete) # Cria o objeto especifico
wesley_fachada = Fachada(wesley)
wesley_fachada.teste_achar_nome()