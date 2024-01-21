# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan

a = float(input('Digite o ângulo desejado: '))
r = radians(a)
s = sin(r)
c = cos(r)
t = tan(r)

print('O Ângulo {:.2f}\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}.'.format(a, s, c, t))

# Obs: Prestar atenção na descrição das funcionabilidades