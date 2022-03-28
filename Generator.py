import random


while True:
    try:
        odp = int(input("Podaj 1 jesli chcesz wygenerowac liste, 2 jesli chcesz z pliku: "))
        if odp == 1:
            break
        elif odp == 2:
            break
        else:
            print("Niepoprawna wartosc.")
    except ValueError:
        print("Niepoprawna wartosc.")

if odp == 1:
    while True:
        try:
            ilosc_wierzcholkow = int(input("Podaj ilosc wierzcholkow: "))
            if ilosc_wierzcholkow > 1:
                break
            else:
                print("Niepoprawna wartosc.")
        except ValueError:
            print("Niepoprawna wartosc.")

    nasycenie = 50
    ilosc_krawedzi = int(nasycenie / 100 * ilosc_wierzcholkow * (ilosc_wierzcholkow - 1) / 2) + 1
    lista_krawedzi = []
    while len(lista_krawedzi) != ilosc_krawedzi:
        krawedz = ([random.randint(1, ilosc_wierzcholkow), random.randint(1, ilosc_wierzcholkow)])
        if krawedz[0] == krawedz[1]:
            continue
        elif krawedz[0] > krawedz[1]:
            krawedz[0], krawedz[1] = krawedz[1], krawedz[0]
        if krawedz not in lista_krawedzi:
            lista_krawedzi.append(krawedz)
    lista_krawedzi.sort()
else:
    f = open("plik.txt", "r")
    lista_krawedzi = []
    ilosc = False
    for i in f:
        #if ilosc != False:
        #   i = i[2:]
        if i != ' ':
            if ilosc == True:
                liczba = ''
                for j in i[:-1]:
                    if j == ' ':
                        liczba = int(liczba)
                        liczba1 = liczba
                        liczba = ''
                    else:
                        liczba = liczba + j    
                i = (liczba1, int(liczba))
                lista_krawedzi.append(i)
            else:
                ilosc_wierzcholkow = int(i)
                ilosc = True
    f.close()

