'''Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
dela e depois mostre se ela pode ou não votar.'''

data = int(input('Digite o seu ano de nascimento:'))
idade = 2023 - data
if idade > 18:
    print('Você tem {} anos de idade e já pode votar!'.format(idade))
else:
    print('Você tem {} anos de idade e ainda não pode votar!'.format(idade))