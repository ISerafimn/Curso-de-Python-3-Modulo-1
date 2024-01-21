# Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite o Primeiro Número: '))
n2 = int(input('Digite o Segundo Número: '))

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 3/10

n3 = n1 + n2

print('O valor da soma entre os valores {} + {} é igual a: \033[35m{}\033[m'.format(n1, n2, n3))
