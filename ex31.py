# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual é a distancia da viagem? '))
if d <= 200:
    v = d * 0.5
else:
    v = d * 0.45
print('O valor da viagem de {:.2f}Km é de R${:.2f}'.format(d, v))

# metodo Guanabara

d = float(input('Qual é a distancia da viagem? '))
v = d * 0.5 if d <= 200 else d * 0.45
print('O valor da viagem de {:.2f}Km é de R${:.2f}'.format(d, v))