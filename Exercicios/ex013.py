# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o salario atual: '))

r = s + ((s / 20) * 3)
# r = s + (s * 15 / 100)

print('O salario de R${:.2f} foi para R${:.2f} depois do reajuste de 15%'.format(s, r))
