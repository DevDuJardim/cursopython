#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boasvindas para ela:
#Ex:
#Qual é o seu nome? João da Silva
#Olá João da Silva, é um prazer te conhecer!

name = input('Qual o seu nome?: ')
print('Olá '+ name.title() + ', é um prazer te conhecer!')

message = 'como é bom telo por aqui!'
print('\nOlá {}, {}'.format(name.title(),message))
 
print('\nOlá ' + name.title() + ', ' + message.upper())