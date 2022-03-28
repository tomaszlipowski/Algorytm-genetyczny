from Generator import ilosc_wierzcholkow, lista_krawedzi


lista_wierzcholkow = list(range(1, ilosc_wierzcholkow + 1))

def dodawanie_koloru(lista_kolorow):
    if lista_kolorow == []:
            lista_kolorow.append(1)
    else:
        lista_kolorow.append(lista_kolorow[-1] + 1)

    return lista_kolorow

def zakazanie(zakazane, lista_krawedzi, wierzcholek, wartosc):
    l = []
    for i in range(len(lista_krawedzi)):
        if wierzcholek == lista_krawedzi[i][0]:
            l.append(lista_krawedzi[i][1])
    counter = 0
    for i in range(len(zakazane)):
        if wartosc == zakazane[i][0]:
            zakazane[i][1] = zakazane[i][1] + l
        else:
            counter += 1
    if counter == len(zakazane):
        zakazane.append([wartosc, l])

    return zakazane

def kolorowanie(lista_krawedzi, lista_wierzcholkow, lista_kolorow):
    zakazane = []
    kolor = False
    for wierzcholek in lista_wierzcholkow:
        licznik = 0
        for e in range(len(zakazane)):
            if wierzcholek in zakazane[e][1]:
                licznik += 1
            else:
                wartosc = zakazane[e][0]
                zakazane = zakazanie(zakazane, lista_krawedzi, wierzcholek, wartosc)
                break
        if licznik == len(lista_kolorow):
            kolor = True
            if zakazane == []:
                wartosc = 1
            else:
                wartosc = zakazane[-1][0] + 1
            zakazane = zakazanie(zakazane, lista_krawedzi, wierzcholek, wartosc)
        if kolor == True:
            lista_kolorow = dodawanie_koloru(lista_kolorow)
            kolor = False

    return lista_kolorow[-1]


ilosc = kolorowanie(lista_krawedzi, lista_wierzcholkow, lista_kolorow = [])


print(f"Zachlanny: {ilosc} kolorow.")
