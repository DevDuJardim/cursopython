#Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório
#entre eles.
#Ex:
#Digite um valor: 8
#Digite outro valor: 5
#A soma entre 8 e 5 é igual a 13.
print('               SOMADOR\n                     ')

valor_01 = float(input('Digite um valor: '))
valor_02 = float(input('Digite outro valor: '))

soma = valor_01 + valor_02
print('A soma entre {} e {} é igual a {}'.format(valor_01,valor_02,soma))