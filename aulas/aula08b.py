import math

num = int(input('Digite um número: '))
# Nome do modulo mais . (ponto final) faz aparecer todas as funcionabilidades do modulo ex: math.
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
# É possivel chamar as funcionabilidades dos modulos de diferças formas exemplo abaixo no math.floor (floor arendonda pra baixo)
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

# Caso não exista a necessidade de todas as funcionabilidades pode sempre usar o from 'modulo' import 'funcionabilide'
from math import sqrt, floor
num = int(input('Digite um número: '))
# note que não existe a necessidade de chamar o .math quando utiliza esse metodo de modulo especifico
raiz = sqrt(num)
aredondado = floor(raiz)
