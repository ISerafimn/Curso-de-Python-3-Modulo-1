v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro : '))
v3 = v1 + v2

print('A soma dos Valor', v1, '+', v2, 'é:', v3)
# Ou
print('A soma dos Valor {} + {} é: {}'.format(v1, v2, v3))

v1 = int(input('Digite o Primeiro Valor (Só números inteiros): '))
v2 = int(input('Digite o Segundo Valor (Só números inteiros): '))
v3 = v1 + v2
print('A Soma dos Dois Valores é', v3)

v1 = float(input('Digite o Primeiro Valor (Aceita Decimal): '))
v2 = float(input('Digite o Segundo Valor (Aceita Decimal): '))
v3 = v1 + v2
print('A Soma dos Dois Valores é', v3)

# Tipo Primivo --> bool <-- ( True || False ) Se digital qualquer coisa = True, se não = False

v1 = str(input('Digite o Primeiro Valor (Visto como Caracter): '))
v2 = str(input('Digite o Segundo Valor (Visto como Caracter): '))
v3 = v1 + v2
print('A Junção dos Dois Valores é', v3)

# Outra forma de Usar o print, as chaves '{}' são trocadas pelo conteúdo dentro dos paranteses do .format
# É possivel adiconar informações depois das chaves {}, conforme o exemplo abaixo

v4 = 1+4
print('A soma vale {}'.format(v4))
print('A soma vale {} (Cinco)'.format(v4))
print('A soma vale {} (seis)'.format('6'))

# 0 comando type mostra qual o tipo da váriavel

n1 = input('Digite um algo: ')
print(type(n1))

print(n1.isnumeric())

# .isnumeric ou .is em geral, aparentemente analisa se tal variavel é ou pode se transformar no que ele cita
