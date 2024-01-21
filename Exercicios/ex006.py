# Crie um algoritimo que leia um número e mostre o seu dobro triplo e raiz quadrada.

v = int(input('Digite um número: '))

d = v * 2
t = v * 3
r = v ** (1/2)

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 6/10
c = '\033[m'
a = '\033[34m'

print('O número {} tem como seu:\ndobro: {},\ntriplo: {}\nraiz quadrada: {}{:.2f}{}.'.format(v, d, t, a, r, c))
