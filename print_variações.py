# -*- coding: utf-8 -*-
"""
Código para aprendizado básico.
1) Tipos de Impressão
"""
a = 10
b = 10.34
c = "python"
d = "é"
e = "fantastico"
f = "c"

print(a) #10
print(type(a)) #<class 'int'>
print('O Valor da Váriável a é: %d' % a) #O Valor da Váriável a é: 10

print(b) #10.34
print(type(b)) #<class 'float'>
print('O Valor da Váriável a é: %f' % b) #O Valor da Váriável a é: 10.340000
print('O Valor da Váriável a é: %.2f' % b) #O Valor da Váriável a é: 10.34

print(type(c)) #<class 'str'>
print(c,d,e)
print(c,d,e, sep=" ", end="!")
print(c) #python é fantastico!python
print(c,d,e, sep="_", end="!\n") #python_é_fantastico!
print(c) #python

print('A linguagem {} é nota {}'.format(c,a))
print('A linguagem {} é melhor que a linguagem {}'.format(c,"c"))
print('A linguagem {} é melhor que a linguagem {}'.format(c,f))
print('A linguagem {1} é melhor que a linguagem {0}'.format(c,f))

print('R$ {}'.format(1.59))
print('R$ {:f}'.format(1.59)) #float
print('R$ {:d}'.format(1)) #inteiro
print('R$ {:.2f}'.format(1.59)) #float com dois números
print('R$ {}'.format(1000.59))
print('R$ {:7.2f}'.format(1000.59)) #com 7 espaços após início, float com 2 casas decimais
print('R$ {:7}'.format(1.59))
print('R$ {:07}'.format(1.59)) #com 7 espaços após início preenchidos com zero
print('Data {:02d}/{:02d}'.format(19,11))

print("'Sim'") #print com aspas
print('"Sim"') #invertido também funciona
print("doesn't") #ou usa aspas duplas
print('doesn\'t') #ou utiliza \' para escapar da aspas simples
print('"doesn\'t", they said') #utilizando aspas duplas e o \' juntos