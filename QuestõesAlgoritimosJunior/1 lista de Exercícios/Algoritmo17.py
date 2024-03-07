Espaco = int(input("Informe o valor do espaco em KM: "))
Tempo = int(input("Informe o valor do tempo em Horas: "))
velocidade = Espaco / Tempo
velocidade_convertida = (Espaco * 1000 ) / (Tempo * 3600)
velocidade3 =  (Espaco/ Tempo) / 3.6
print(f'A velocidade do seu objeto em KM/H sera:{velocidade}')
print(f'A velocidade do objeto em M/S sera:{velocidade_convertida:.2f}')
print(f'A velocidade do objeto em M/S sera:{velocidade3:.2f}')


