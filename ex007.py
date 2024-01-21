# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 7/10

print('A média da nota do aluno com as menções {:.1f} e {:.1f} é: {}{:.1f}{}!'.format(n1, n2, '\033[7;33m', m, '\033[m'))
