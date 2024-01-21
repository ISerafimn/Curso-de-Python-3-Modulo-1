# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 9/10
v = int(input('Digite o número da tabuada desejada: \033[33m'))

print('{} x  0 = {}'.format(v, 0 * v))
print('{} x  1 = {}'.format(v, 1 * v))
print('{} x  2 = {}'.format(v, 2 * v))
print('{} x  3 = {}'.format(v, 3 * v))
print('{} x  4 = {}'.format(v, 4 * v))
print('{} x  5 = {}'.format(v, 5 * v))
print('{} x  6 = {}'.format(v, 6 * v))
print('{} x  7 = {}'.format(v, 7 * v))
print('{} x  8 = {}'.format(v, 8 * v))
print('{} x  9 = {}'.format(v, 9 * v))
print('{} x 10 = {}\033[m'.format(v, 10 * v))
