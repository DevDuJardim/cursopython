#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
#seu novo salário, com 15% de aumento.
print('      AUMENTO DE SALÁRIO\n         ')

nome = input('Nome do funcionario: ')
salario_1 = float(input('Digite o salário atual do funcionario: R$ '))
aumento = float(input('Porcentagem do aumento: '))

fracao = salario_1 * aumento/100
salario_novo = salario_1 + fracao

print('O novo salário do funcionário {} é de R$ {}.'.format(nome.title(),salario_novo))