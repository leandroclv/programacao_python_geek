dias = int(input('Digite quantos dias trabalhado: '))
valor = dias * 30
desc = valor - (valor * 0.08)
print(f'A quantia bruta é R${valor:.2f} e com 8% de imposto fica R${desc:.2f}.')