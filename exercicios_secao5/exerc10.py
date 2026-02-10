altura = float(input('Digite a sua altura: '))
sexo = str(input('Digite o seu sexo [F/M]: '))[0]
if sexo in ('mM'):
    peso = (72.7 * altura) - 58
    print(f'O peso ideal para você é {peso:.2f}!')
if sexo in ('Ff'):
    peso = (62.1 * altura) - 44.7
    print(f'O peso ideal para você é {peso:.2f}!')