#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
#segundo grau e mostre o valor de Delta.

print('     VALOR DE DELTA\n     ')

valor_A = float(input('Digite o valor A: '))
valor_B = float(input('Digite o valor B: '))
valor_C = float(input('Digite o valor C: '))

delta = valor_B ** 2 - 4 * (valor_A * valor_C)
print(delta)