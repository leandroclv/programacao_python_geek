idade = int(input('Digite a idade do nadador: '))
if idade > 5:
    if 5 < idade < 7:
        print('O nadador está na categoria Infantil A!')
    elif 8 < idade < 10:
        print('O nadador está na categoria Infantil B!')
    elif 11 < idade < 13:
        print('O nadador está na categoria Juvenil A!')
    elif 14 < idade < 17:
        print('O nadador está na categoria Juvenil B!')
    elif idade > 18:
        print('O nadador está na categoria Sênior!')
else:
    print('Idade inferior para fazer natação')
