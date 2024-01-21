# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido
import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

e = random.choices([a1, a2, a3, a4])

print('O aluno ganhador foi o {}. Parabens!!!'.format(e))

# Metodo Guanabara
# Lista, no caso agrupamento de variaveis, tem que ser contina em colchetes []

lista = [a1, a2, a3, a4]
e = random.choice(lista)
print('O aluno escolhido foi {}'.format(e))
