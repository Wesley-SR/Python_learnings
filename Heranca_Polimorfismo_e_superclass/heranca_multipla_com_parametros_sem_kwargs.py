# Olhar: https://www.youtube.com/watch?v=tX_v8dgb_7I

class Pai:
    def __init__(self, nome_pai, idade_pai, **kwargs):
        print('Construindo a classe Pai')

        super().__init__(**kwargs)
        self.nome_pai = nome_pai
        self.idade_pai = idade_pai
        self.frase_pai = 'Pai eh pai'



class Mae:
    def __init__(self, nome_mae, idade_mae, **kwargs):
        print('Construindo a classe Mae')

        super().__init__(**kwargs)
        self.nome_mae = nome_mae
        self.idade_mae = idade_mae
        self.frase_mae = 'Mae eh mae'


class Filha(Pai, Mae):
    def __init__(self, np, nm, nf, ip, im, idf):
        print('Construindo a classe filha')

        super().__init__(nome_pai = np, nome_mae = nm, idade_pai = ip, idade_mae = im)

        self.nome_filha = nf
        self.idade_filha = idf
        # print('O nome do pai é:  ', self.nome_pai)
        # print('O nome da mae é:  ', self.nome_mae)
        # print('Frase pai: ', self.frase_pai)
        # print('Frase mae: ', self.frase_mae)    
    
    def print_names(self):
        print('\n')
        print('Nome da filha:  ', self.nome_filha)
        print('O nome do pai é:  ', self.nome_pai)
        print('O nome da mae é:  ', self.nome_mae)
        print('\n')


    def print_idades(self):
        print('Idade da filha:  ', self.idade_filha)
        print('A Idade do pai é:  ', self.idade_pai)
        print('A Idade da mae é:  ', self.idade_mae)
        print('\n')

    def print_frases(self):
        print('Frase pai: ', self.frase_pai)
        print('Frase mae: ', self.frase_mae)
        print('\n')
 


if __name__ == "__main__":  

    # nome_pai = 'Joao'
    # nome_mae = 'Maria'
    # nome_filha = 'Jorgia'
    # idade_pai = 50
    # idade_mae = 40
    # idade_filha = 15

    # Filha(nome_pai, nome_mae, nome_filha, idade_pai, idade_mae, idade_filha)
    # jorgia1 = Filha(nome_pai, nome_mae, nome_filha, idade_pai, idade_mae, idade_filha)

    # jorgia1.print_names()
    # jorgia1.print_frases()
    # jorgia1.print_idades()

    np = 'Joao'
    nm = 'Maria'
    nf = 'Jorgia'
    idp = 50
    idm = 40
    idf = 15

    jorgia2 = Filha(np, nm, nf, idp, idm, idf)
    # jorgia2 = Filha(nome_pai = np, nome_mae = nm, nome_filha = nf, idade_pai = idp, idade_mae = idm, idade_filha = idf)
    jorgia2.print_names()
    jorgia2.print_frases()
    jorgia2.print_idades()
