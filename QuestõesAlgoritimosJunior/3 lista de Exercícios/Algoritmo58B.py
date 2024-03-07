listaVogais = ['A','E','I','O','U']
Caracteres = ['@','#','%','&','*','!','?','[]','{}']
Numeros = ['1','2','3','4','5','6','7','8','9','10','11']
letra = input("Digite uma letra: ")
letra = letra.upper()
if letra in listaVogais:
    print(f'Sua letra {letra} é uma vogal')
elif letra in Caracteres:
    print(f'Letra digitada não é  cosoante e nem vogal')
elif letra in Numeros:
    print("Voce digitou um numero e não uma letra")
else:
    print(f'Sua letra {letra} é uma consoante')
