num = int(input('Escolha um numero inteiro: '))
print('''Escolha um a das bases para converter:
Para converter em Binario digite [1]
Para converter em Octaginal digite [2]
Para converter em Hexadecimal digite [3]
 ''')
opção = int(input('Digite sua opção: '))
if opção == 1:
    print('{} em binario é igual a {}.'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} em octal é igual a {}.'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} em Hexdecimal éigual a {}.'.format(num,hex(num)[2:]))
else:
    print('Opção invalida!')
