class Animal():
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor
        self.__fome = False

    def pedir_comida(self, tipo_comida):
        self.__tipo_comida = tipo_comida
        self.__fome = True
        print(f"{self.__nome} está com fome e quer {self.__tipo_comida} ")

    def comer(self):
        if self.__fome == True:
            print(f"O {self.__nome} está comendo")

        else:
            print(f'O {self.__nome} não está com fome')


class Cachorro(Animal):
    def __init__(self, nome, cor, dono):
        super().__init__(nome, cor) # Herdando tudo da classe Animal(nome, cor)
        self.__dono = dono

    def latir(self, nome):
        print(f' O {nome} diz:  Au au au')

lolita = Cachorro('Lolita', 'marrom', 'Jessica')
