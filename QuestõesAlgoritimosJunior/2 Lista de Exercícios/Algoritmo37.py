salario = float(input("Informe seu salario: "))
if salario < 500:
    reajuste = salario * 1.15

elif salario >= 500 and salario <= 1000:
    reajuste = salario * 1.1

else:
    reajuste = salario * 1.05
    
print(f'Seu novo salario sera:{reajuste}')