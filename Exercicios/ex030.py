# Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro: '))

r = n % 2

if r == 0:
    print('O número {} é Par'.format(n))
else:
    print('O número {} é IMPAR'.format(n))
