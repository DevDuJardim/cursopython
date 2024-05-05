'''Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.'''

from random import randint

print("Jogo da adivinhação")

num_sort = randint(1,5)
print("Tente acertar o numero entre 1 e 5")

num = int(input("Escolha o numero:"))

print("Você escolheu {}".format(num))

print("O pc sorteou o numero {}".format(num_sort))

if num == num_sort:
    print("Você acertou!!")
else:
    print("Você errou!")


