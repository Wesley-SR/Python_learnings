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


class Pessoa():
    def __init__(self, nome, idade):
        self.nome_pessoa = nome
        self.comida_favorita = 'Costela assada'
        # Um método que herda a classe "Pessoa" tem acesso a comida favorita
        self.__bebida_favorita = 'Agua'
        # Apenas um método interno da classe "Pessoa" tem acesso a bebida favorita
        print('Construindo a classe Mae')
        print('O nome da pessoa é  ', nome)
        print('A idade da pessoa é ', idade)

    def diz_bebida_favorita(self):
        print('Minha bebida favorita é ', self.__bebida_favorita)
   
class Homem(Pessoa):
    def __init__(self, nome, idade): # self, nome, idade
        super().__init__(nome, idade)
        self.__cabelo_da_namorada = 'Castanho escuro'
        self.__cort = None 

    def confere_canivete(self, canivete):
        if canivete == 'Victor_Inox':
            self.__cort = self.cortar_corda
        if not canivete == 'Victor_Inox':
            self.__cort = self.cortar_sabao

    def cortar_corda(self):
        print('Cortando corda')
    def cortar_sabao(self):
        print('Cortando sabao')

    def cortar(self, canivete):
        self.confere_canivete(canivete)
        self.__cort()




nome_pessoa = 'Wesley'
idade_pessoa = '23'
#marca_canivete = 'Victor_Inox'
marca_canivete = 'Marca_capeta'

wesley = Homem(nome_pessoa, idade_pessoa)

wesley.cortar(marca_canivete)