# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10
# exercicios passados número: 2/10

limpar = '\033[m'
cor = {
    'azul': '\033[34m',
    'vermelho': '\033[31m',
    'amarelo': '\033[33m',
    'verde': '\033[32m'}

nome = input('Digite o seu nome: ')
nome = nome + '!'
print('É um prazer te conhecer,', nome)

# Método do Guanabara

nome = input('Digite o seu nome: ')
print('É um prazer te conhecer, {}{}{}!'.format(cor['azul'], nome, limpar))
