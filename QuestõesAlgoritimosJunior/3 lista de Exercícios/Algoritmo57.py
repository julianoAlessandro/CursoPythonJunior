p1 = float(input("Informe o valor do primeiro produto:"))
p2 = float(input("Informe o valor do segundo produto:"))
descontop1 = p1 * 0.86 #desconto de 14%
descontop2 = p2 * 0.83  #desconto de 17%
valor = p1 * 0.14 #corresponder ao valor de 14% do produto
valor2 = p2 * 0.17 #corresponder ao valor de 17% do produto
print(f'O primeiro produto com desconto de 14% fica {descontop1}, sendo que voce economizou {valor: .2f}')
print(f'O segundo produto com desconto de 17% fica {descontop2}, sendo que voce economizou {valor2:.2f}')
  