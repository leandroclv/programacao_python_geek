venda_mensal = float(input('Digite qual foi a sua venda mensal: R$'))
if venda_mensal >= 100000:
    comissao = 700 + (venda_mensal * 0.16)
    print(f'A comissão do vendedor será de R${comissao:.2f}')
if 100000 > venda_mensal >= 80000:
    comissao = 650 + (venda_mensal * 0.14)
    print(f'A comissão do vendedor será de R${comissao:.2f}')
if 80000 > venda_mensal >= 60000:
    comissao = 600 + (venda_mensal * 0.14)
    print(f'A comissão do vendedor será de R${comissao:.2f}')
if 60000 > venda_mensal >= 40000:
    comissao = 550 + (venda_mensal * 0.14)
    print(f'A comissão do vendedor será de R${comissao:.2f}')
if 40000 > venda_mensal >= 20000:
    comissao = 500 + (venda_mensal * 0.14)
    print(f'A comissão do vendedor será de R${comissao:.2f}')
if venda_mensal < 20000:
    comissao = 400 + (venda_mensal * 0.14)
    print(f'A comissão do vendedor será de R${comissao:.2f}')
