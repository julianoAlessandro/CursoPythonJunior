def CalcularPA(a1,r, Q):
    ListaPA = []
    PAImpares = []
    PAPares = []
    somaPA = []
    for n in range(2,Q):
        An = a1 + (n - 1) * r
        ListaPA.append(An)
        if An % 2 != 0:
            PAImpares.append(An)
        else:
         PAPares.append(An)
    for impar, par in zip (PAImpares, PAPares):
         soma = impar + par
         somaPA.append(soma)

    print(f'LISTA DE PA {ListaPA}')
    print(f'LISTA DE PA IMAPRES {PAImpares}')
    print(f'LISTA DE PA PARES{PAPares}')
    print(f'SOMA DE LISTA PAR E IMPAR{somaPA}')


CalcularPA(8,3,10)