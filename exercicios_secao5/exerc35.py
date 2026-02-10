dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
if dia <= 31:
    if mes <= 12:
        if (mes == 2) or (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            if dia <= 30:
                if (mes == 2) and (ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0):
                    if dia < 30:
                        print(f'A data {dia}/{mes}/{ano} está válida!')
                    else:
                        print('Dados inválidos')
            else:
                print('Dados inválidos')
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            if dia <= 31:
                print(f'A data {dia}/{mes}/{ano} está válida!')
            else:
                print('Dados inválidos')
        else:
            print('Dados inválidos')
    else:
        print('Dados inválidos')
else:
    print('Dados inválidos')
