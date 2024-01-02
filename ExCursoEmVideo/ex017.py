#Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
#80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

vel = float(input('Digite a velocidade: '))
if vel > 80:
    print('Você foi multado!')
multa = (vel-80)*5
print('O valor da multa é de R$ {:.2f}'.format(multa))
