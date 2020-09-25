'''
Except = Exceto (Advérvio) ou Excecutar (Verbo)
Raise = Levantar (Verbo)
Assert = Afirmar
'''

#  ------------- Tratamento de exceções -------------
def testetipo():
    x = int(input('Digite um numero  '))
    print(type(x))

def testeassert1():

    for y in range(5):
        x = int(input('Por favor, informe um número: '))
        assert (type(x) == int or type(x) == float), TypeError
        assert (x >= 10 and x <= 20), Exception
        assert (x >= 15 and x < 30), "Fora do intervalor"

    print ('Passou tudo')

def testetry1():
    print('testetry2')
    y = 0
    for y in range(5):
        try:
            x = int(input("Por favor, informe um número: "))
            a = 1/x
        # Se ocorrer uma exceção pula para fora do FOR, não faz sentido usar o TRY nesse caso

        except ZeroDivisionError as error:
            print('Tipo do erro:  ', error)
            print("Descrição do erro:  Divisão por zero, ta loco?")

        except ValueError as error:
            print('Tipo do erro:  ', error)
            print("Descrição do erro:  Não foi um número válido!")

    print('O for terminou')

def testetry2():
    print('testetry2')
    try:
        y=0
        for y in range(5): 
            x = int(input("Por favor, informe um número: "))
            a = 1/x
    # Se ocorrer uma exceção pula para fora do FOR, não faz sentido usar o TRY nesse caso

    except ZeroDivisionError as error:
        print('Tipo do erro:  ', error)
        print("Descrição do erro:  Divisão por zero, ta loco?")

    except ValueError as error:
        print('Tipo do erro:  ', error)
        print("Descrição do erro:  Não foi um número válido!")

    print('O for terminou')

#  ------------- Levantando exceções -------------
def raise_disparando1():
    raise ValueError('Digite o numero certo')
    # A exceção é disparada de qualquer jeito

def raise_disparando2(x):
    print(type(x))
    num = int(x)
    if x > 10:
        raise Exception('Valor maior que 10')

def raise_disparando3():
    '''
    Neste exemplo quando a exception é disparada o código nõa continua rodando
    e trava.
    '''
    print('raise_disparando3')
    y=0
    for y in range(5):
        x = int(input("Por favor, informe um número: "))

        if x > 50 and x < 100:
            raise Exception(' 50 < x < 100')
        if x >= 100 and x < 150:
            raise ValueError(' 100 <= x < 150')

        print('Ok!')
        

        print('y =  ',y)
    print('Acabou o for')


def testetry_com_raise(x):
    print('testetry2')
    y = 0
    for y in range(5):
        try:
            a = 1/x
            if x > 10 and x < 20:
                raise Exception(' 50 < x < 100')
            if x >= 20 and x < 30:
                raise ValueError(' 100 <= x < 150')
            print('Ocorreu tudo certo!')
        # Se ocorrer uma exceção pula para fora do FOR, não faz sentido usar o TRY nesse caso

        except ZeroDivisionError as error:
            print('Tipo do erro:  ', error)
            print("Descrição do erro:  Divisão por zero, ta loco?")

        except ValueError as error:
            print('Tipo do erro:  ', error)
            print("Descrição do erro:  Não foi um número válido!")

        except Exception as error:
            print('Tipo do erro:  ', error)
            print("Descrição do erro:  Não foi um número válido!")
            
    print('O for terminou')


def type_and_range_checker(command, new_angle):
    if not (type(new_angle) == int or type(new_angle) == float):
        raise TypeError('The new_angle variable must be either'
                        ' int or float')
    if command == 'pan':
        if not (new_angle > 0 and new_angle < 360):
            raise ValueError('Desired pan angle out of range')

    elif command == 'tilt':
        if (new_angle > 90) and (new_angle < 311):
            raise ValueError('Desired tilt angle in dead zone')
        elif (new_angle < -49) or (new_angle >= 360):
            raise ValueError('Desired tilt angle out of range')
        elif (new_angle >= -49) and (new_angle < 0):
            new_angle = new_angle + 360  # For negative angle

    print('Entrada de comando e ângulo, ok!')

def test_checker_com_try():
    for a in range(5):
        print('a =  ', a)
        try:
            type_and_range_checker('pan', 1000)

        except ZeroDivisionError as error:
            print('ZeroDivisionError')
            print("Description error:  ", error)

        except ValueError as error:
            print('ValueError')
            print("Description error:  ", error)
        except TypeError as error:
            print('TypeError')
            print("Description error:  ", error)

    print('Terminou o FOR')

def test_checker_sem_try():
    for a in range(5):
        print('a =  ', a)
        type_and_range_checker('tilt', 1000)


#testeassert1()
#raise_disparando2(2)
#testetry1()
#testetry2()
#aise_disparando3()
testetry_com_raise(11)
#test_checker_com_try()