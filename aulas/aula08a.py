# O termo import chama modulos/bibliotecas ex: import aula06a chama todos os dados do arquivo aula06a
# É possivel importar bibliotecas/modulos já existentes no sistema como o import math que adicona varios termos de matematica
# 'from aula06a import variavel1' basicamente é um import que busca um dado especifico dentro do modulo que nesse caso é a aula06a

#'import' modulo completo
import math

#'from' para coisas especificas do modulo
from math import ceil

# 'ceil' é um termo do import math, ele aredonda para cima qualquer valor
d = ceil(4 + 5.4)
print(d)