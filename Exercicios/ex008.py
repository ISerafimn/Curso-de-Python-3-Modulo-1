# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 8/10
m = float(input('\033[36mDigite a metragem:\033[m '))

c = m * 100
mm = m * 1000

print('A metragem {}m convertida em centimetros é igual a: {}cm e convertida em milímetros é: {}mm'.format(m, c, mm))
