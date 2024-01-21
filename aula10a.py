tempo = int(input('Quantos anos tem o seu carro? '))

# O if e else do python precisa colocar : (dois pontos) após a condição

if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')

print('--FIM--')

# Condição simplificada

tempo = int(input('Quantos anos tem o seu carro? '))

print('Carro Novo' if tempo <= 3 else 'Carro Velho')

print('--FIM--')
