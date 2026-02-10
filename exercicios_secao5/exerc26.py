dist = float(input('Digite a quilometragem da distância (km): '))
gas = float(input('Digite a quantidade de litros consumido pelo carro: '))
consumo = dist/gas
if consumo < 8:
    print('Venda o carro!')
elif 8 < consumo < 14:
    print('Econômico!')
elif consumo > 12:
    print('Super econômico!')