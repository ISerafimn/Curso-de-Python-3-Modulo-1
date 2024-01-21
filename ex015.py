# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

km = float(input('Quantos Kms foram percorridos com o carro? '))
dias = int(input('Quantos dias foi alugado o carro? '))

t = (km * 0.15) + (dias * 60)

print('O custo total foi de: R${:.2f}'.format(t))
