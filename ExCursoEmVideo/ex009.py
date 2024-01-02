#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
#e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5,42.

print('        CONVERSOR DE DOLLAR\n           ')

real = float(input('Digite quanto você tem em Real: R$ '))
dollar = real/5.42

print('Isso te daixa com US$ {}, Dollares'.format(dollar))