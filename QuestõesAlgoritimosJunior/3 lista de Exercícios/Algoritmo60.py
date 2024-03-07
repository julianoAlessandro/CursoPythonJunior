nome = input("Informe seu nome:")
n1 = float(input("Informe a sua nota: "))
n2 = float(input("Informe a sua nota: "))
n3 = float(input("Informe a sua nota: "))
media = (n1 + n2 + n3)/3
if media > 7:
    print(f'parabéns {nome} voce foi aprovado')
elif media < 7 and media > 5:
    print(f'voce ficou com media: {media:.2f} e esta de recuperação')
else:
    print(f'{nome} voce esta reprovado!')