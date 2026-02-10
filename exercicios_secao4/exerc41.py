hora = float(input('Digite o valor de hora de trabalho: R$'))
mes = int(input('Digite as horas trabalhandas: '))
salario = hora * mes
adici = salario + (salario * 0.10)
print(f'O salário do funcionário que trabalhou {mes} horas irá receber R${adici:.2f} com 10% adicional.')