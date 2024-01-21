nome = input('Qual é o seu Nome? ')

# a expressão {:'qualquer número'} delimita o numero minimo de caracteres utilizados, caso não
# haja o suficiente é completado com espaços vazios
print('Prazer em te conhecer {:20}!'.format(nome))

# dependendo do simbolo atribuido a variavel é alinhada em uma posição: > (direita), < (esquerda), ^ (centro).
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))

#se for adicionado um caracter ao lado do : (caso o alinhamento seja o central (^), ele se repetira
# até completar a área vazia

print('Prazer em te conhecer {:a^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
