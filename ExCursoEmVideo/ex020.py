'''Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
ÍMPAR.'''
print('      PAR OU IMPAR\n      ')

num = int(input('Digite um numero inteiro:'))
if num % 2 == 0:
    print('O numero {} é um numero par.'.format(num))
else:
    print('O numero {} é um numero impar'.format(num))