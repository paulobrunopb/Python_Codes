# -*- coding: utf-8 -*-
"""
Created on Sat Fev  12 14:50:00 2022

https://www.digitalocean.com/community/tutorials/como-fazer-um-programa-de-calculadora-simples-no-python-3-pt

CALCULADORA BÁSICA
"""
# Abertura do programa
def welcome():
    print('''
Bem vindo a Calculadora Básica 1.0
''')

# Criando a função calculate()
def calculate():
    operation = input('''
Escolha o tipo de Operação Matemática que deseja realizar:
+ for Adição
- for Subtração
* for Multiplicação
/ for Divisão
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    #Adição
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    #Subtração
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    #Multiplicação
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    #Divisão
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou uma operação matemática válida, por favor inicie o programa novamente.')
    #Função again()
    again()

# Criando a função again() que permite utilizar a calculadora novamente
def again():
    calc_again = input('''
Deseja calcular novamente??
Digite S para Sim ou N para Não
''')

    # se Sim
    if calc_again.upper() == 'S':
        calculate()

    # Se Não
    elif calc_again.upper() == 'N':
        print('''
O programa será encerrado
Até mais!
''')
    
    # Se o usuário digitar outro valor, reiniciar a função again()
    else:
        again()

welcome()
calculate()