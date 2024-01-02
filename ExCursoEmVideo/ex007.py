#Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a
#sua terça parte.
#Ex:
#Digite um número: 3.5
#O dobro de 3.5 é 7.0
#A terça parte de 3.5 é 1.16666

print('      DOBRO/TERÇA PARTE\n           ')

number = float(input('Digite um numero: '))

dobro = number * 2
terca = number / 3

print('O dobro de {} é {}.\nA terça parte de {} é {}.'.format(number,dobro,number,terca))