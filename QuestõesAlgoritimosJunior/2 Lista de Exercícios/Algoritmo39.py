peso = float(input("Informe seu peso em KG:"))
altura = float(input("Informe sua altura em Metros:"))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu imc é:{imc:.2f}, de acordo com a tabela voce esta ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
     print(f'Seu imc é:{imc:.2f}, de acordo com a tabela voce  tem PESO NORMAL')
elif imc >= 25 and imc < 30:
      print(f'Seu imc é:{imc:.2f}, de acordo com a tabela voce  tem SOBREPESO')
elif imc >= 30 and imc <= 35:
     print(f'Seu imc é:{imc:.2f}, de acordo com a tabela voce  tem OBESIDADE')
else:
     print('Voce tem Obesidade de grau elevado')


