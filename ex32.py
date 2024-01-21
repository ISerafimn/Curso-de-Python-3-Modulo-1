# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

a = input('Digite um ano: ')

if a == 0 or a == '':
    a = date.today().year
else:
    a = int(a)

if a % 100 == 0:
    if a % 400 == 0:
        print('O ano {}, é bissexto!'.format(a))
    else:
        print('O ano {}, não é bissexto!'.format(a))
else:
    if a % 4 == 0:
        print('O ano {}, é bissexto!'.format(a))
    else:
        print('O ano {}, não é bissexto!'.format(a))

# Metodo Guanabara

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano {}, é bissexto!'.format(a))
else:
    print('O ano {}, não é bissexto!'.format(a))
