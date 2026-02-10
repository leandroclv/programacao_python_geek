a = int(input('Digite o 1° número inteiro: '))
b = int(input('Digite o 2° número inteiro: '))
c = int(input('Digite o 3° número inteiro: '))
operacao = int(input('''Escolha qual operação você quer: 
Geométrica: 1
Ponderada:  2
Harmônica:  3
Aritmética: 4
Opção: '''))
if 0 < operacao < 5:
    if operacao == 1:
        geo = a * b * c ** (1/3)
        print(f'O resultado da operação de Geometria é {geo:.2f}!')
    elif operacao == 2:
        pon = ((a + 2) * (b + 3))/ 6
        print(f'O resultado da operação Ponderada é {pon:.2f}!')
    elif operacao == 3:
        har = 1/((1/a) + (1/b) + (1/c))
        print(f'O resultado da operação Harmônica é {har:.2f}!')
    else:
        ari = (a + b + c)/3
        print(f'O resultado da operação Aritmética é {ari:.2f}!')
else:
    print('Escolha errada!')