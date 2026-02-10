soma = 0
for i in range(1, 11):
    x = int(input(f'Digite o {i}° número para a média: '))
    soma = soma + x
print(f'A méida dos números digitados é {soma/10}')
