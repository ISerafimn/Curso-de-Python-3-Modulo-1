# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

s = float(input('Digite o seu salário atual: R$'))

if s >= 1250:
    a = (s / 10) + s
    print('O salário anterior de R${:.2f}, teve um aumento de 10% sendo o valor atual o de R${:.2f}.'.format(s, a))
else:
    a = ((s / 20) * 3) + s
    print('O salário anterior de R${:.2f}, teve um aumento de 15% sendo o valor atual o de R${:.2f}.'.format(s, a))