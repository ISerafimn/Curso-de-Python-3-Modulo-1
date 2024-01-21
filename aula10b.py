n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m <= 4:
    print('Reprovou')
elif m <= 6:
    print('Recuperação')
else:
    print('Passou')

print('A sua Media é igual á: {:.f}'.format(m))
