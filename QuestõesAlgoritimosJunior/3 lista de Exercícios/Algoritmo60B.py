nome = input("Informe seu nome:")
Notas = []
for nota in range(1,4):
    notas = float(input(f"{nota})informe sua nota:"))
    Notas.append(notas)

media = sum(Notas)/3
if media > 7:
    print(f'parabéns {nome} voce foi aprovado')
elif media < 7 and media > 5:
    print(f'voce ficou com media: {media:.2f} e esta de recuperação')
else:
    print(f'{nome} voce esta reprovado!')
