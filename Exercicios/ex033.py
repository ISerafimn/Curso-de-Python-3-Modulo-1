# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 > n3:
    print('O maior número é o {}, e o menor é o {}'.format(n1, n3))
elif n2 > n1 > n3:
    print('O maior número é o {}, e o menor é o {}'.format(n2, n3))
elif n3 > n2 > n1:
    print('O maior número é o {}, e o menor é o {}'.format(n3, n1))
elif n2 > n3 > n1:
    print('O maior número é o {}, e o menor é o {}'.format(n2, n1))
elif n1 > n3 > n2:
    print('O maior número é o {}, e o menor é o {}'.format(n1, n2))
else:
    print('O maior número é o {}, e o menor é o {}'.format(n3, n2))