#Crie um programa que leia o nome e o salário de um funcionário, mostrando no
#final uma mensagem.
#Ex:
#Nome do Funcionário: Maria do Carmo
#Salário: 1850,45
#O funcionário Maria do Carmo tem um salário de R$1850,45 em Junho.

name = input('Nome do Funcionario: ')
sal = input ('Salário: R$ ')

print('O funcionario ' + name.title() + ', tem o salário de R$ ' + sal +' em Junho.')
print('\nO funcionario {}, tem o salário de R$ {}, em junho.'.format(name.title(),sal))