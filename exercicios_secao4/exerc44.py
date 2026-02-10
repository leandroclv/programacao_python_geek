degrau = int(input('Digite a altura do degrau em cm: '))
escada = int(input('Digite a altura da escada em m: '))
total = escada / (degrau / 100)
print(f'Como a escada possue uma altura de {escada}m e a dos degraus {degrau}cm, será necessário {total} degraus para alcançar essa altura da escada.')