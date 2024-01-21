print('\033[0;30;41mOlá Mundo!')

# Basicamente a troca da cor do style, do texto e do fundo é representado por '/033[style;texto;fundom'
# Após o valor do fundo é necessario colocar a letra m e alí por diante pode seguir o texto do print

print('\033[0;30;41mOlá Mundo!\033[m')

# para para a alteração do 'tema' é necesario fechar com \033[m

a = 2
b = 3
print('Os valores são \033[32m{}\033[m e logo em seguida \033[35m{}\033[m'. format(a, b))

# é possivel adicionar mais de uma cor em determinadas partes do mesmo print, também é possivel alterar
# apenas um ou mais parametro dos 3 possiveis
nome = 'Igor'

# Usar o .format para a estilização das cores

print('Meu nome é {}{}{}'.format('\033[35m', nome, '\033[m'))

limpar = '\033[m'
azul = '\033[34:40m'

# Organizar as cores por lista chamando o nome delas dentro da lista

cores = {
    'azul': '\033[34:40m',
    'vermelho': '\033[31:40m',
    'amarelo': '\033[33:40m',
    'verde': '\033[32:40m' }

print('Meu nome é {}{}{}'.format(azul, nome, limpar))
print('Meu nome é {}{}{}'.format(cores['vermelho'], nome, limpar))