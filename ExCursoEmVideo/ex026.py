'''Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
- O primeiro valor é o maior
- O segundo valor é o maior
- Não existe valor maior, os dois são iguais'''
print('                   MAIOR NUMERO                  ')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('Primeiro valor: {}\nSegundo valor {}'.format(n1,n2))

if n1 > n2 :
    print('O primeiro valor é o maior!')
elif n1 < n2:
    print('O segundo numero é o maior!')
else:
    print('Não existe valor maior, os valores são iguas!')