# Crie um programa que leia o número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127, o número 6.127 tem a parte inteira 6.]

import math

n1 = float(input('Digite um número Real (com casa decimal): '))
print('O valor digitado foi {} a porção inteira é {:.0f}'.format(n1, n1))

# Metodo Guanabara
# math.trunc delimita para a exibição de apenas a porção inteira (aparentemente nivela para baixo)

print('O valor digitado foi {} a porção inteira é {}'.format(n1, math.trunc(n1)))
# ou
print('O valor digitado foi {} a porção inteira é {}'.format(n1, int(n1)))

# Obs: O metodo utilizando o {:.0} nivela utilizando as regras de aredondamento
