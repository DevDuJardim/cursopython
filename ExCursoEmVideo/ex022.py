'''Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
- Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
alistamento.'''
from datetime import date
print('         ALISTAMENTO MILITAR\n          ')

ano_nas = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nas
print('Quem nasceu em {} completa {} anos de idade em {}.'.format(ano_nas,idade,ano_atual) )

if idade < 18: 
    print('Ainda faltam {} anos para seu alistamento'.format(18-idade))
    print('Seu alistamento será em {}.'.format((18-idade)+ano_atual))
elif idade > 18:
    print('Você ja deveria ter se alistado há {}')

