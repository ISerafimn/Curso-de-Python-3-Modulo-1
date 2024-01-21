# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

v1 = random.randint(0, 5)

v2 = int(input('Escolha um número de 0 a 5: '))

if v1 == v2:
    print('O valor sorteado foi {}, você acertou!!!'.format(v1))
else:
    print('O valor sorteado foi {}, você errou!!!'.format(v1))

#metodo guanabara
print('Processando...')
sleep(2)
if v1 == v2:
    print('O valor sorteado foi {}, você acertou!!!'.format(v1))
else:
    print('O valor sorteado foi {}, você errou!!!'.format(v1))