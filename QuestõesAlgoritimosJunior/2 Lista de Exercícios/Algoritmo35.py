distancia = int(input("Informe a distancia percorrida em KMs: "))
Combustivel = int(input ("Informe a quantidade de combustível em Listros: "))
ConsumoMedio  = distancia / Combustivel
print(f'Seu consumo médio sera:{ConsumoMedio:.2f} KM/L')