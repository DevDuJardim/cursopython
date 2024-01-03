'''[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
de cada lado deve ser menor que a soma dos outros dois.'''
print('        CRIADOR DE TRIANGULO\n       ')

print('Analise retas para formar um triangulo:')
reta_1 = float(input('Valor da reta 1: '))
reta_2 = float(input('Valor da reta 2: '))
reta_3 = float(input('Valor da reta 3: '))
if (reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and (reta_2 + reta_3 > reta_1):
    print('Você pode ter um triangulo')
else:
    print('Você não pode ter um quadrado!')