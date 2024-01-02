#Crie um programa que leia o preço de um produto, calcule e mostre o seu
#PREÇO PROMOCIONAL, com 5% de desconto.

print('      PREÇO PROMOCIONAL\n        ')

prod = float(input('Digite o preço do produto: R$ '))
des = int(input('Porcentagem do desconto: '))

porcentagem = prod*des/100
preco_final = prod - porcentagem

print('Com desconto de R$ {}, o preço final é de R$ {}'.format(porcentagem,preco_final))