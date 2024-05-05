'''Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)'''

from random import randint

print ("_________JOKEN PO_____________")

print("\nFaça sua jogada!\n")

Jogada_pc = randint(1,3)

jogador = int(input("[1] = Pedra. \n[2] = Papel. \n[3] = Tesouora\n"))
print("")

if jogador == 1:
    print("Você escolheu PEDRA!")
elif jogador == 2:
    print("Você escolheu PAPEL!")
elif jogador == 3:
    print("Você escolheu TESEOURA!")

print("")

if Jogada_pc == 1:
    print("Jogada do pc PEDRA!")
elif Jogada_pc == 2:
    print("Jogada do pc PAPEL!")
elif Jogada_pc == 3:
    print("Jogada do pc TESEOURA!\n")

if (jogador == 1) and (Jogada_pc == 3) or (jogador == 2) and (Jogada_pc == 1) or (jogador == 3) and (Jogada_pc == 2):
    print("\nJogador Venceu!\n")
elif (jogador == Jogada_pc):
    print("\nEmpate!\n")
else:
    print("\nPC Venceu!\n")