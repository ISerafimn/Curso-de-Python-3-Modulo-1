# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Digite a velocidade do carro: '))

if v > 80:
    m = (v - 80) * 7
    print('Você ultrapssou o limite de velocidade, você será multado em {}'.format(m))
else:
    print('Tudo nos conformes')
