# Crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre
# quantos dólares ela pode comprar.

# Considere que US$1.00 = R$3.27

v = float(input('Digite o quanto dinheiro você tem: R$'))

d = v * 3.27

print('Seus R${:.2f} convertidos em dólar é igual a: US${:.2f}'.format(v, d))
