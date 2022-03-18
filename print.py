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

print(a) #10
print(type(a)) #<class 'int'>
print('O Valor da Váriável a é: %d' % a) #O Valor da Váriável a é: 10

print(b) #10.34
print(type(b)) #<class 'float'>
print('O Valor da Váriável a é: %f' % b) #O Valor da Váriável a é: 10.34
print('O Valor da Váriável a é: %.2f' % b) #O Valor da Váriável a é: 10.34

print(type(c)) #<class 'str'>
print(c,d,e, sep=" ", end="!")
print(c) #python é fantastico!python
print(c,d,e, sep="_", end="!\n") #python_é_fantastico!
print(c) #python