#!/usr/bin/env python3

"""
    Comando para executar $  python3 testArg.py -l 10 -c 10
    Obs.: Se executar em passar os parametros ou sem expecificar
    vai dar erro.
"""

import argparse
parser = argparse.ArgumentParser(description='Calcular a área de um terreno')

# Adicionar os argumentos posicionais
parser.add_argument('-l','--largura', type = int, help = 'Largura do terreno')
parser.add_argument('-c','--comprimento', type = int, help = 'Comprimento do terreno')

args = parser.parse_args()

def calcula_area(largura,comprimento):
    area = largura*comprimento
    return area

if __name__ == '__main__':
    resultado_area = calcula_area(args.largura, args.comprimento)
    print("Largura: {}".format(args.largura))
    print("Comprimento: {}".format(args.comprimento))
    print("Area: {}".format(resultado_area))
