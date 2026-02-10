n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° núemro: '))
n3 = int(input('Digite o 3° número: '))
maior = n1
if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3
menor = n1
if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3
meio = n1
if (menor < n2 < maior):
    meio = n2
if (menor < n3 < maior):
    meio = n3
print(f'Os número em ordem crescentes são {menor}, {meio} e {maior}!')