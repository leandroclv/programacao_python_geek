print('''Preço antigo          - Percentual de aumento
até R$ 50             - 5%
até R$ 50 e R$ 100    - 10%
acima de R$ 100       - 15%''')
print('-*-' * 20)
print('''Preço novo            - Mensagem
até R$ 80             - Barato
entre R$ 80 e R$ 120  - normal
entre R$ 120 e R$ 200 - caro
acima de R$ 200       - muito caro''')
preco = float(input('Digite o preço antigo do produto: R$'))
if preco < 50:
    preco_novo = preco + (preco * 0.05)
if 50 < preco < 100:
    preco_novo = preco + (preco * 0.10)
else:
    preco_novo = preco + (preco * 0.15)
if preco_novo < 80:
    print(f'O novo preço do produto R$ {preco_novo:.2f} é barato!')
elif 80 < preco_novo <= 120:
    print(f'O novo preço do produto R$ {preco_novo:.2f} é normal!')
elif 120 < preco_novo <= 200:
    print(f'O novo preço do produto R$ {preco_novo:.2f} é caro!')
else:
    print(f'O novo preço do produto R$ {preco_novo:.2f} é muito caro!')
