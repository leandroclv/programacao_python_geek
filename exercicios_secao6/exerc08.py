maior = menor = 0
for x in range(1, 11):
    number = int(input(f'Digite o {x}° número: '))
    if number > maior:
        maior = number
    elif number < menor:
        menor = number
print(f'O maior número foi {maior} e o menor {menor}.')
