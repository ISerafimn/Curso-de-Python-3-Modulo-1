# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um número inteiro: '))

suc = n1 + 1
ant = n1 - 1

print('O número {} tem como seu sucessor: {} e como seu antecessor: {}.'.format(n1, suc, ant))

# Metodo guanabara

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 5/10

n1 = int(input('Digite um número inteiro: '))
print('O n° {}{}{} tem como sucessor: {} e seu antecessor: {}.'.format('\033[31m', n1, '\033[m', (n1 + 1), (n1 - 1)))
