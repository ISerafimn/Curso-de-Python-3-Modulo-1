# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Digite o preço atual do produto: R$'))

d = v - (v / 20)

print('O preço caiu de R${:.2f} para R${:.2f} (5% de desconto)'.format(v, d))
