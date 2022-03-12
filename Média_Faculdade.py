# -*- coding: utf-8 -*-
"""
CALCULADORA DE APROVAÇÃO DE FACULDADE

Created on Fri Jun 11 22:41:31 2021

@author: paulo
"""

media = float(input('Informe a sua média: '))

if (media >= 7):
    print('Você está aprovado(a)!')
    print('Parabéns!')
elif (media >= 4):
    print('Você está na final...')
else:
    print('Você está reprovado(a)!')