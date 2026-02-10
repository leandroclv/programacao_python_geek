salario = float(input('Digite o valor do salário: R$'))
receber = salario + (salario * 0.05) - (salario * 0.07)
print(f'O funcionário que possui um salário de R${salario:.2f}, possui uma gratificação de 5% e paga de imposto 7% irá ter no salário final R${receber:.2f}.')