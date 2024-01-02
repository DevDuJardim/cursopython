#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
#um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
#sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

print('      LOCADORA DE VEICULOS\n          ')

km_rd = float(input('Distanci percorrida em KM: '))
dias_alu = int(input('Dias alugados: '))

km_pg = km_rd * 0.20
dias_pg = dias_alu * 90
valor_final = km_pg + dias_pg

print('Preço D/alugados: R$ {}.\nPreço KM/rodados R$ {}.\nValor final a pagar: R$ {}.'.format(dias_pg,km_pg,valor_final))
