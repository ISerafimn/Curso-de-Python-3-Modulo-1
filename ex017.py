# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa;
import math

co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))

h = (co ** 2 + ca ** 2) ** (1/2)

print('O Cateto Oposto {} e o Cateto Adjacente {} tem como Hipotenusa o valor de {:.2f}!'.format(co, ca, h))

# Metodo Guanabara
# math.hypot calcula a hipotenusa

h = math.hypot(co, ca)

print('O Cateto Oposto {} e o Cateto Adjacente {} tem como Hipotenusa o valor de {:.2f}!'.format(co, ca, h))
