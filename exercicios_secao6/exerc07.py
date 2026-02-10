x = 1
soma = 0
while x <= 10:
    number = int(input(f'Digite o {x}° número: '))
    if number > 0:
        soma = soma + number
        x += 1
    else:
        continue
print(f'A média dos números positivos é {soma/10}')
