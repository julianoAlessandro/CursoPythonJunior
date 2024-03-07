precoProduto = float(input("Informe o preço do produto: "))
DescontoProduto = precoProduto * 0.9 # Com 10% de desconto
economia = (precoProduto * 10 )/ 100 # quanto economizou 10 % do produto
print(f'O valor do produto é:{precoProduto}R$, já o seu produto com desconto de 10% fica{DescontoProduto}R$,sendo que com 10% voce economiza {economia}R$')