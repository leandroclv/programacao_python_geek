escolha = int(input(("""Escolha a opção:
1 - Soma de 2 números.
2 - Diferença entre 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero).
Opção: """)))
if 0 < escolha < 5:
    n1 = int(input('Digite o 1° valor: '))
    n2 = int(input('Digite o 2° valor: '))
    if escolha == 1:
        print(f'A soma dos dois números é {n1 + n2:.2f}.')
    elif escolha == 2:
        maior = n1
        if (n2 > maior):
            maior = n2
        menor = n1
        if (n2 < menor):
            menor = n2
        print(f'A subtração do {maior} pelo {menor} é {maior - menor}.')
    elif escolha == 3:
        print(f'O resultado da multiplicação dos números é {n1 * n2}.')
    else:
        if n2 != 0:
            print(f'O resultado da divisão dos dois números é {n1/n2}.')
        else:
            print('O denominador não pode ser zero.')
else:
    print('Escolha inválida.')