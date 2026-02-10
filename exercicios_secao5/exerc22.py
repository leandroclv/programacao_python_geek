idade = int(input('Digite a sua idade: '))
tempo = int(input('Digite o tempo de serviço: '))
if (idade >= 65) or (tempo >= 30) or (idade >= 60 and tempo >= 25):
    print('Você pode se aposentar.')
else:
    print('Você não pode se aposentar.')
