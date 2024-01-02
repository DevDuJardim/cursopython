#Crie um programa que leia o número de dias trabalhados em um mês e mostre o
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
#por hora trabalhada.
print('      CALCULO DE SALÁRIO\n        ')

name = input('Nome do funcinario: ')
dias_tra = int(input('Dias trabalhados: '))

horas_dia = dias_tra * 8
preco_dia = horas_dia * 7.50

print('O funcionario {}, trabalhou {} dias neste mês. e seu salário é igual a: R$ {}'.format(name.title(),dias_tra,preco_dia))