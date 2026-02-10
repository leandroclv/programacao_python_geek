altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
if (altura < 1.2) and (peso < 60):
    print('Você foi classificado na classe A')
elif (1.2 < altura <= 1.7) and (peso < 60):
    print('Você foi classificado na classe B')
elif (altura > 1.7) and (peso < 60):
    print('Você foi classificado na classe C')
elif (altura < 1.2) and (60 < peso <= 90):
    print('Você foi classificado na classe D')
elif (1.2 < altura <= 1.7) and (60 < peso <= 90):
    print('Você foi classificado na classe E')
elif (altura > 1.7) and (60 < peso <= 90):
    print('Você foi classificado na classe F')
elif (altura < 1.2) and (peso > 90):
    print('Você foi classificado na classe G')
elif (1.2 < altura <= 1.7) and (peso > 90):
    print('Você foi classificado na classe H')
elif (altura > 1.7) and (peso > 90):
    print('Você foi classificado na classe I')
