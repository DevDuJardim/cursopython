print('       EMPRESTIMO CASA\n          ')
valor = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o salário: R$ '))
ano_pg = (int(input('Em quantos anos pretende pagar: ')))

val_par = valor / (ano_pg * 12)

terço = sal*30/100
if val_par > terço:
    print('Emprestimo negado.')
if val_par < terço:
    print('Seu emprestimo foi aprovado com parcelas de R$ {:.2f} por mês.'.format(val_par))
