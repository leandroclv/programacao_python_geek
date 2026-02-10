valor = float(input('Digite o valor do produto: R$'))
est = int(input('''Digite o estado 
MG - 1
SP - 2
RJ - 3
MS - 4
: '''))
if 0 < est < 5:
    if est == 1:
        valor = valor + (valor * 0.07)
        print(f'O valor do produto no estado de Minas Gerais é de R${valor:.2f}.')
    elif est == 2:
        valor = valor + (valor * 0.12)
        print(f'O valor do produto no estado de São Paulo é de R${valor:.2f}.')
    elif est == 3:
        valor = valor + (valor * 0.15)
        print(f'O valor do produto no estado do Rio de Janeiro é de valor R${valor:.2f}.')
    else:
        valor = valor + (valor * 0.08)
        print(f'O valor do produto no estado do Mato Grosso do Sul é de valor R${valor:.2f}.')
else:
    print('valor iválido')
