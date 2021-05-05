
''' Jeito mais trabalho, mas evita conflitos de funções '''
import uteis

num = int(input('Digite um valor: '))

fat = uteis.fatorial(num)
print('O fatorial de {} eh {}'.format(num, fat))

dob = uteis.dobro(num)
print('O dobro de {} eh {}'.format(num, fat))

metad = uteis.metade(num)
print('A metade de {} eh {}'.format(num, fat))


# ''' Jeito simplificado mas não recomendado '''
# from uteis import fatorial, dobro, metade

# num = int(input('Digite um valor: '))

# fat = fatorial(num)
# print('O fatorial de {} eh {}'.format(num, fat))

# dob = dobro(num)
# print('O dobro de {} eh {}'.format(num, fat))

# metad = metade(num)
# print('A metade de {} eh {}'.format(num, fat))