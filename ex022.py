# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas
# * O nome com todas minúsculas
# * Quantas letras ao todo (sem considerar espaços)
# * Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ').strip()

print('Nome com todas as letras Maiúsculas:', nome.upper())
print('Nome com todas as letras Minúsculas:', nome.lower())

noSpace = nome.replace(' ', '')
# print('O número de caracteres sem contar o espaço(s) é:', len(noSpace))
print('O número de caracteres é: {}, sem contar o espaço(s).'.format(len(noSpace)))

lista = nome.split()
print('O número de caracteres no primeiro nome é:', len(lista[0]))

# Metodo guanabara

print('O número de caracteres é: {}, sem contar o espaço(s).'.format(len(nome) - nome.count(' ')))
