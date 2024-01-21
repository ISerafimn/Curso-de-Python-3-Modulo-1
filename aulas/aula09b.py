frase = str('Curso em Video Python')
print(frase)

# o [] logo após a variavel fatiara converme o caracter selecionado, caso exista dois valores separados
# por : (dois pontinhos) ele selecionara tudo entre esses caracteres
print(frase[6])
print(frase[6:14])

# Caso não exista um numero antes dos : (dois pontos) ele puxara todos os caracteres até o
# número selecionando, o inverso tambem funciona
print(frase[:6])
print(frase[6:])

# caso coloque ::2 (dois ou outro valor) determinara quantas casas será puladas na leitura, nesse caso de duas em duas
print(frase[::2])

# ao usar  o print(""" ~~~~~~~~ TEXTO ~~~~~~~~~ """) é possivel conter numa unica print um texto de varias
# linhas, ele mantem as quenra de linhas

print("""Em um dia ensolarado
Fernandinho se perdeu
ele vagou e vagou mas continuou perdido""")

# basicamente separei a frase usando o split e puxei no print apenas a primeira palavra que foi separa
# com o primeiro [] e no segundo [] eu selecionei o caracter que quero ver dessa frase
dividido = frase.split()
print(dividido[0][3])
