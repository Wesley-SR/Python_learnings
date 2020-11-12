class Pai():
    def __init__(self, nome, idade):
        self.__comida_favorita = 'Massas'
        quantidade_de_casas = 2
        print('Construindo a classe Pai')
        print('O nome do pai é:  ', nome)
        print('A idade do pai é:  ', idade)
    
class Mae():
    def __init__(self, nome, idade):
        self.__comida_favorita = 'Bolo'
        quantidade_de_casas = 2
        print('Construindo a classe Mae')
        print('O nome da mae é:  ', nome)
        print('A idade da mae é:  ', idade)
    
class Filha(Mae):
    def __init__(self, nome_mae, nome_filha, idade_mae, cpf):
        super().__init__(nome_mae, idade_mae)
        print('Nome da filha:  ', nome_filha)
        print('O cpf da filha é:  ', cpf)

class HerdaDuas(Mae, Pai):
    def __init__(self, nome_mae, nome_filha, idade_mae, cpf):
        super().__init__(nome_mae, idade_mae)
        print('Nome da filha:  ', nome_filha)
        print('O cpf da filha é:  ', cpf)


nome_mae = 'Maria'
nome_filha = 'Jeorgia'
idade_mae = 40
cpf_filha = 123456789

nome_pai = 'Joao'
idade_pai = 50

primeira_filha = Filha(nome_mae, nome_filha, idade_mae, cpf_filha)

segunda_filha = HerdaDuas(nome_mae, nome_filha, idade_mae, cpf_filha)