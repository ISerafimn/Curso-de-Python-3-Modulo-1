frase = str('Curso em Video Python')
print(frase)

# len analisa o numero de caracter dentro de uma variavel
print(len(frase))

# .count conta quantos dos caracteres selecionados a variavel tem, no caso do exemplo é o caracter 'o'
print(frase.count('o'))

# definição do parametro/fatiamento que será considerado, neste caso do exemplo, o caracter 'o', da casa ou caracter
# zero ao 13 da variavel
print(frase.count('o', 0, 13))

# .find encontra o momento (posição) do parametro desejado, caso não exista o valor do parametro será mostrado -1
print(frase.find('deo'))

# in, basicamento responde com true para existe dentro do caracter e False para caso não exista o
# parametro digitado antes de 'in'
print('curso' in frase)
print('banana' in frase)

# .replace muda os caracteres selecionados dentro da variavel por outros, a mudança não altera a variavel, só o
# que é mostrado na 'print' atual
print(frase.replace('Python', 'Android'))
print(frase)

# se conter o frase.replace dentro de outra variavel ou na mesma referenciada o texto é de fato alterado exemplo abaixo
alterada = frase.replace('Python', 'Android')
print(alterada)

# ------------- Formatação de Caracter ------------------------------

# .upper deixa todos os caracteres em maiusculo
print(frase.upper())

# .lower deixa todos os caracteres em minusculo
print(frase.lower())

# .capitalize deixa todos os caracteres em minusculo exceto o primeiro que fica em maiusculo
print(frase.capitalize())

# .title transforma os primeiros caracteres(letras) de todas as palavras em maisculo e o
# restante dos caracteres em minusculo
print(frase.title())

frase = '   Aprenda Python  '
print(frase)

# .strip remove todos os espaços excedentes no começo e final da variavel/frase contida na variavel
# .rstrip remove os espaços apenas da direira/right
# .lstrip remove os espeços apenas da esquerda/left
print(frase.strip())

# ------------------ Dividir String -------------------

frase = 'Curso em Video Python'

# .split, basicamente divide a frase pelos seus espeços, no caso da frase 'Curso em Video Python' ela será dividida
# em 4 partes distintas e a contagem de caracter é individual para cada pedaço, ele cria uma especie de lista
print(frase.split())
frase2 = frase.strip()
print(frase2)

# .join basicamente coloca o caracter selecionado a frente, exemplo o '-' entre cada caracter da frase
print('-'.join(frase))
