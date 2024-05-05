'''[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes'''

print('Analise retas para formar um triangulo:')
reta_1 = float(input('Valor da reta 1: '))
reta_2 = float(input('Valor da reta 2: '))
reta_3 = float(input('Valor da reta 3: '))
if (reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and (reta_2 + reta_3 > reta_1):
    print('Você pode ter um triangulo')
else:
    print('Você não pode ter um quadrado!')

if(reta_1 == reta_2) and (reta_2 == reta_3):
    print('Seu triangulo é Equilátero!')
elif(reta_1 == reta_2) or (reta_1 == reta_3) or (reta_2 == reta_3):
    print("Seu triangulo é Isóceles! ")
elif(reta_1 != reta_2) and (reta_1 != reta_3) and (reta_2 != reta_3):
    print("Seu triangulo e Escaleno!")