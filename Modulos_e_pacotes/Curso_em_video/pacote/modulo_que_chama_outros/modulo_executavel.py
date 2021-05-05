''' Utilizando o sys.path.insert '''
import sys
caminho = "/home/wesley/Desktop/Wesley/Python_learnings/Modulos_e_pacotes/Curso_em_video/pacote"
sys.path.insert(0, caminho)

from numeros import operacoes

num = int(input('Digite um valor: '))

fat = operacoes.fatorial(num)
print('O fatorial de {} eh {}'.format(num, fat))

dob = operacoes.dobro(num)
print('O dobro de {} eh {}'.format(num, dob))

metad = operacoes.metade(num)
print('A metade de {} eh {}'.format(num, metad))