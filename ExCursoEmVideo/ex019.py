'''Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
não um bom aproveitamento (se ficou acima da média 7.0).'''

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2
if media >= 7:
    print('Sua média foi {}, parabens pelo desempenho! '.format(media))
else:
    print('sua média foi {}, esforce-se mais!'.format(media))