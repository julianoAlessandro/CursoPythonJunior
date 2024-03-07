contador = 0
Numeros = []
while contador < 5:
    contador = contador + 1
    valor = int(input(f"{contador})Digite o valor a ser guardado:"))
    Numeros.append(valor)

media = sum(Numeros)/len(Numeros)
print(f'A media de valores sera:{media}')