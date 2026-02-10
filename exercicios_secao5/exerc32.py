pedido = int(input('''Especificação   - código - Preço
Cachorro Quente - 100    - 1.20
Bauru Simples   - 101    - 1.30
Bauru com Ovo   - 102    - 1.50
Hamburguer      - 103    - 1.20
Cheeseburguer   - 104    - 1.70
Suco            - 105    - 2.20
Refrigerante    - 106    - 1.00
Pedido pelo código: '''))
if 100 < pedido < 107:
    quantidade = int(input('Qual a quantidade: '))
    if pedido == 100:
        print(f'Você pediu {quantidade} de Cachorro quente e o preço total será R${quantidade * 1.20:.2f}')
    elif pedido == 101:
        print(f'Você pediu {quantidade} de Bauru Simples e o preço total será R${quantidade * 1.30:.2f}')
    elif pedido == 102:
        print(f'Você pediu {quantidade} de Bauru com Ovo e o preço total será R${quantidade * 1.50:.2f}')
    elif pedido == 103:
        print(f'Você pediu {quantidade} de Hamburger e o preço total será R${quantidade * 1.20:.2f}')
    elif pedido == 104:
        print(f'Você pediu {quantidade} de Cheeseburguer e o preço total será R${quantidade * 1.70:.2f}')
    elif pedido == 105:
        print(f'Você pediu {quantidade} de Suco e o preço total será R${quantidade * 2.20:.2f}')
    else:
        print(f'Você pediu {quantidade} de Refrigerante e o preço total será R${quantidade * 1.00:.2f}')
else:
    print('Dados do pedido inválidos')
