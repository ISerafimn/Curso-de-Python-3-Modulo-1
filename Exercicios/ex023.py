# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# unidade = 4, dezena = 3, centena = 8 e milhar = 1;

valor = input('Digite um número de 0 a 9999: ')
separar = ' '.join(valor).split()

print('unidade:', separar[3])
print('dezena:', separar[2])
print('centena:', separar[1])
print('milhar:', separar[0])

# metodo guanabara

num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))

# Obs: O meu não funcionou perfeiitamente, ele buga em valores menores de 1000, quatro digitos