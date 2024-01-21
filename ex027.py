# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
# nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite o seu nome: ').strip().split()

print('Primeiro:', nome[0])
print('Último:', nome[-1])

# -1 busca o ultimo elemento de uma lista
