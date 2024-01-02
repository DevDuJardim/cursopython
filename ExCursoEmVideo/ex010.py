#Faça um algoritmo que leia a largura e altura de uma parede, calcule e
#mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
#sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

print('          CALCULO DE AREA          ')

altura = float(input('Digite altura: '))
largura = float(input('Digite a largura: '))

area = altura * largura
tinta = area/2

print('O calculo total da area da parede é de {} m2 e será gasto {} litros de tinta para pintura.'.format(area,tinta))