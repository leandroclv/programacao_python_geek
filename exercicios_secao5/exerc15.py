num = int(input('Digite um número de 1 a 7 para escolher o dia da semana: '))
if 0 < num < 8:
    if num == 1:
        print('Domingo')
    elif num == 2:
        print('Segunda')
    elif num == 3:
        print('Terça')
    elif num == 4:
        print('Quarta')
    elif num == 5:
        print('Quinta')
    elif num == 6:
        print('Sexta')
    else:
        print('Sábado')
else:
    print('Dados inválidos!')