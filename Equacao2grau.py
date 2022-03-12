"""
Created on Sat Jan  8 20:10:00 2022

@author: paulo

Instruções:
1. Peça que o usuário digite o valor dos coeficientes do polinômio (a, b, c) e armazene-os em variáveis
2. Crie uma função que receba os três coeficientes do polinômio e retorne:
    2.1. Duas raízes reais, caso o Delta seja maior que zero;
    2.2. Uma raiz real, caso o Delta seja igual a zero;
    2.3. Duas raízes complexas, caso o Delta seja menor do que zero;
3. Ao retornar essas raízes, imprima-as no console
4. Ao imprimir na tela, pergunte se o usuário deseja continuar
5. Caso o usuário deseje continuar retorne ao passo 1.
6. Caso o usuário não deseje continuar, envie uma mensagem ao usuário e encerre o programa.
"""
from math import sqrt

# Abertura do programa
def welcome():
    print('''
Bem vindo a Calculadora de Raízes do 2º Grau 1.0
''')


def calcular_raizes(a, b, c):
    raizes = []
    
    delta = b**2 - (4 * a * c)
    
    if (delta >0):
        # Duas raízes reais e distintas
        raiz1 = (-b + sqrt(delta)) / (2 *a)
        raiz2 = (-b - sqrt(delta)) / (2 *a)
        
        raizes.append(raiz1)
        raizes.append(raiz2)
    elif (delta == 0):
        # Duas raízes reais e iguais
        raiz = -b / (2 * a)
        
        raizes.append(raiz)
    else:
        # Duas raízes complexas
        raiz1 = complex( -b / (2 * a), sqrt(abs(delta)) / (2 * a) )
        raiz2 = complex( -b / (2 * a), sqrt(abs(delta)) / (2 * a) )
        
        raizes.append(raiz1)
        raizes.append(raiz2)
        
    return raizes
        
continuar = 'S'

welcome()

while (continuar.upper() == 'S'):
    a = float(input('Informe o valor do coeficiente a: '))
    b = float(input('Informe o valor do coeficiente b: '))
    c = float(input('Informe o valor do coeficiente c: '))
    
    raizes = calcular_raizes(a, b, c)
    
    if (len(raizes) == 1):
        print('x =', raizes[0])
    else:
        print('x1 =', raizes[0])
        print('x2 =', raizes[1])
        
    continuar = input('Deseja continuar [S/N]? ')
    
print('O programa será encerrado')