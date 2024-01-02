from random import randint
from time import sleep
print('-'*20)
computador = randint(0,5)
jogador = int(input('escolha seu numero:' ))
print('Processando...')
sleep(2)

if jogador == computador:
    print('Eu escolhi {},você ganhou!'.format(computador))
else:
    print('Eu escolhi {}, Você perdeu!'.format(computador))

