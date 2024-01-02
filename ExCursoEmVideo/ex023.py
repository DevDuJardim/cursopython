'''Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que leia nome,
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que:
- Homens ganham 5% de desconto
- Mulheres ganham 13% de desconto'''

print('          DIA DAS MULHERES\n         ')
nome = input('Digite seu nome: ')
print('''Digite:
    [1] Para Homem
    [2] Para Mulher
      ''')
escolha = int(input('escolha:'))
val = float(input('Digite o valor da compra: R$ '))
des_h = val*5/100
des_m = val*13/100
if escolha == 1:
    print('Olá {}, o preço final é de {:.2f}.'.format((nome.title()),val-des_h))
elif escolha == 2:
    print('Olá {}, o preço final é de {:.2f}'.format((nome.title()),val-des_m))
else:
    print('Erro...')
