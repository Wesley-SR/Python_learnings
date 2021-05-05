#!/usr/bin/env python3

import argparse
parser = argparse.ArgumentParser(description='Calcular a área de um terreno')

# Adicionar os argumentos posicionais
parser.add_argument('largura', type = int, help = 'Largura do terreno')
parser.add_argument('comprimento', type = int, help = 'Comprimento do terreno')

args = parser.parse_args()

def calcula_area(largura,comprimento):
    area = largura*comprimento
    return area

if __name__ == '__main__':
    resultado_area = calcula_area(args.largura, args.comprimento)
    print("Largura: {}".format(args.largura))
    print("Comprimento: {}".format(args.comprimento))
    print("Area: {}".format(resultado_area))
