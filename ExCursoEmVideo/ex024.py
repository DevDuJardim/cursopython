'''Faça um algoritmo que pergunte a distância que um passageiro deseja
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
viagens até 200Km e R$0.45 para viagens mais longas.'''
print('         PASSAGEM\n         ')
print('''---------------------------------------------
        Calcule o preço da passagem:''')
dis_km = float(input('\nDistancia em Km: '))
menor200 = dis_km * 0.5
maior200 = dis_km * 0.45
if dis_km <= 200:
    print('O valor da passagem será R$ {:.2f}.'.format(menor200))
else:
    print('O valor da passagem será R$ {:.2f}'.format(maior200))
