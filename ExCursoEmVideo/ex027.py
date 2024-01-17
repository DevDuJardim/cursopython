'''Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média até 4.9: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
print('               MÉDIA\n                 ')

nota_01 = float(input('Digite a primeira nota: '))
nota_02 = float(input('Digite a segunda nota: '))

media = (nota_01 + nota_02) / 2

if media < 4.9:
    print('Sua média é {}, e você esta REPROVADO!'.format(media))
elif (media >= 5.0) and (media <= 6.9):
    print('Sua média é {}, e voê está em RECUPERAÇÃO'.format(media))
else:
    print('Sua média é {}, e você está APROVADO!'.format(media))