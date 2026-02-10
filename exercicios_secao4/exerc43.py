preco = float(input('Qual o valor da compra: R$'))
total_10 = preco - (preco * 0.10)
valor_parc = preco / 3
vende_vista = total_10 * 0.05
vende_parc = preco * 0.05
print(f'O preço do produto é R${preco:.2f}, com desconto de 10% fica R${total_10:.2f}. Se o cliente deseja pode parcelar em 3x sem juros com cada parcela de R${valor_parc:.2f}. Se a compra for feita à vista o vendedor receberá de comissão R${vende_vista:.2f}, caso seja parcelado receberá R${vende_parc:.2f}.')
