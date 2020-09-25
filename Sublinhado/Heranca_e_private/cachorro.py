import animal

class Cachorro(animal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self, nome):
        print(f' O {nome} diz:  Au au au')