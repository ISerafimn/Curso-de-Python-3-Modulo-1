n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
md = n1 % n2

# a chave com o {:.'algum numero'f} ou {:.5f} delimita a quantidade de numero decimais mostrado,
# nesse caso do exemplo é 5 numeros flot. Obs: funciona sem o f de flot

print('A soma é: {}, a subtração é: {}, a multiplicação é: {} e a divisão é {:.3f}'.format(a, s, m, d))

# o termo end='' impede a quebra de linha e o termo \n quebra a linha
print('A divisão inteira é: {},\nexpoente é: {}\nmodulo é: {}'.format(di, e, md), end='; ')
print(' Calculos Concluidos!')