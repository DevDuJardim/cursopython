#[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
#fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
#quantos dias de vida um fumante perderá e exiba o total em dias.
print('     CALCULO DE REDUÇÃO DE VIDA\n        ')

cig_dia = int(input('Numero de cigarros fumados por dia: '))
anos_fum = int(input('Anos de fumante: '))

cig_fum = cig_dia * (anos_fum * 365)
dia_lost = 144
dias_perd = cig_fum/dia_lost
anos_perd = dias_perd/365
print('\nVocê perdeu {} dias fumando!'.format(dias_perd))