Numeros = []
for numero in range(1,4):
    numero = int(input(f"{numero})Informe um número:"))
    Numeros.append(numero)

Soma = sum(Numeros)
media = Soma/ len(Numeros)
print(f'Sua media:{media:.2f}')