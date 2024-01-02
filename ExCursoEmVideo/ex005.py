#Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
#na tela a sua média na disciplina.
#Ex:
#Nota 1: 4.5
#Nota 2: 8.5
#A média entre 4.5 e 8.5 é igual a 6.5
print('           MÉDIA             \n')

print('Declare as notas do aluno abaixo.')
nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
nota_3 = float(input('Terceira nota: '))
nota_4 = float(input('Quarta nota: '))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print('A média do aluno é {}.'.format(media))