import random
certa = 0
errada = 0
n1 = random.randint(1,100)
n2 = random.randint(1,100)
quest1 = int(input(f'Qual é a soma de {n1} + {n2}? '))
resp1 = n1 + n2
if quest1 == (n1 + n2):
    certa += 1
else:
    errada += 1
n1 = random.randint(1,100)
n2 = random.randint(1,100)
quest2 = int(input(f'Qual é a soma de {n1} + {n2}? '))
resp2 = n1 + n2
if quest2 == (n1 + n2):
    certa += 1
else:
    errada += 1
n1 = random.randint(1,100)
n2 = random.randint(1,100)
quest3 = int(input(f'Qual é a soma de {n1} + {n2}? '))
resp3 = n1 + n2
if quest3 == (n1 + n2):
    certa += 1
else:
    errada += 1
n1 = random.randint(1,100)
n2 = random.randint(1,100)
quest4 = int(input(f'Qual é a soma de {n1} + {n2}? '))
resp4 = n1 + n2
if quest4 == (n1 + n2):
    certa += 1
else:
    errada += 1
n1 = random.randint(1,100)
n2 = random.randint(1,100)
quest5 = int(input(f'Qual é a soma de {n1} + {n2}? '))
resp5 = n1 + n2
if quest5 == (n1 + n2):
    certa += 1
else:
    errada += 1
print(f'Sua resposta da 1° questão foi {quest1} e a resposta certa foi {resp1}')
print(f'Sua resposta da 2° questão foi {quest2} e a resposta certa foi {resp2}')
print(f'Sua resposta da 3° questão foi {quest3} e a resposta certa foi {resp3}')
print(f'Sua resposta da 4° questão foi {quest4} e a resposta certa foi {resp4}')
print(f'Sua resposta da 5° questão foi {quest5} e a resposta certa foi {resp5}')
print(f'você acertou {certa} e errou {errada}!')