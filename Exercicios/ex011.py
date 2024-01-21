# Faça um programa que leia a altura e a largura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

a = float(input('Em metros, digite a altura da parede: '))
la = float(input('Em metros, digite a largura da parede: '))

ar = a * la
t = ar / 2

print('A parede de {} por {}, tem como área total o valor de: {}m² e '
      'necessita {:.1f} litros de tinta'.format(a, la, ar, t))
