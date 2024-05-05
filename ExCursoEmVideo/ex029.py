'''Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
- Até 3 anos de empresa: aumento de 3%
- entre 3 e 10 anos: aumento de 12.5%
- 10 anos ou mais: aumento de 20%'''

print("___________REAJUSTE DE SALÁRIO________________")

nome = input("Nome do funcionário: ")
salario = float(input("Salário do funcionário: R$ "))
tempo_de_casa = int(input("Tempo de casa: "))

print("Ofuncionário {}, recebe R${} de salário e trabalha na empresa a {} anos.".format(nome,salario,tempo_de_casa))

if tempo_de_casa <= 3:
    acrecimo = salario * 3 / 100
    print("Seu novo salário é de R$ {}.".format(salario + acrecimo))
elif tempo_de_casa <= 10:
    acrecimo = salario * 12.5 / 100
    print("Seu novo salário é de R$ {}.".format(salario + acrecimo))
else:
    acrecimo = salario * 20 / 100
    print("Seu novo salário é de R$ {}.".format(salario + acrecimo))