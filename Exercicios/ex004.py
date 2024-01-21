# Faça um programa que leia algo pelo teclado e mosre na tela o seu tipo primitivo e
# todas as informações possiveis sobre ela.
# Sistema de Cores pre feito na aula 11, desafio: utilizar cores em no minimo 10 exercicios passados número: 4/10
dado = input('\033[45mDigite algo:\033[m ')
 
print(dado)
print(type(dado))

print('É um número? ', dado.isnumeric())
print('É alfanúmerico? ', dado.isalnum())
print('Está no alfabeto? ', dado.isalpha())
print('É ASCII? ', dado.isascii())
print('É um digito? ', dado.isdigit())
print('É decimal? ', dado.isdecimal())
print('É um identificador? ', dado.isidentifier())
print('É todo em formato minusculo? ', dado.islower())
print('É considerado um titulo? ', dado.istitle())
print('É todo em espaço? ', dado.isspace())
print('É todo em formarto maiusculo? ', dado.isupper())
print('É possivel imprimir? ', dado.isprintable())
