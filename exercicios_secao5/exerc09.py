salario = float(input('Digite o salário do trabalhador: R$'))
valor_prestação = float(input('Qual o valor da prestação do emprestimo: '))
if valor_prestação > (salario * 0.20):
    print('Empréstimo não consedido')
else:
    print('Empréstimo consedido')