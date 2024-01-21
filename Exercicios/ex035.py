# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem
# ou não formar um triângulo

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 10/10
limpar = '\033[m'
cor = {
    'azul': '\033[34m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'verde': '\033[32m'}

n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))

if n3 < n1 + n2 and n2 < n3 + n1 and n1 < n3 + n2:
    print('{}{}{}, é possivel transformar em um triângulo!'.format(cor['verde'], 'SIM', limpar))
else:
    print('{}{}{}, Não é possivel transformar em um triângulo!'.format(cor['vermelho'], 'NÃO', limpar))
