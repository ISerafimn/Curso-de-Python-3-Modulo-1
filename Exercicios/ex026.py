# Faça um programa que leia uma frase pelo teclado e mostre:
# * Quantas vezes aparece a letra "A";
# * Em que posição ela aparece na primeira vez;
# * Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantidade de letra "A" na frase:', frase.count('A'))
print('Posição da primeira letra "A":', frase.find('A'))
print('Posição da última letra "A":', frase.rfind('A'))
