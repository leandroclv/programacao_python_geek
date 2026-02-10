valor = float(input('Digite o valor do produto: R$'))
desc = valor - (valor * 0.12)
print(f'O valor do produto foi R${valor:.2f} e com desconto de 12% ficou R${desc:.2f}')