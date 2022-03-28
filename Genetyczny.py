from Zachlanny import lista_krawedzi, ilosc, lista_wierzcholkow, ilosc_wierzcholkow
import random
import copy


def funkcjaKosztu(lista_krawedzi, dziecko, F):
    if F:
        del dziecko[:2]
    funkcja = 0
    d = 0
    for krawedz in lista_krawedzi:
        if dziecko[krawedz[0] - 1] == dziecko[krawedz[1] - 1]:
            funkcja += 2
            d = 1
    k = len(list(dict.fromkeys(dziecko)))**2
    funkcja = funkcja + d + k
    dziecko.insert(0, k)
    dziecko.insert(0, funkcja)

    return dziecko

def jakieKolory(dziecko3):
    kolory_set = set(dziecko3[2:])
    return list(kolory_set)

def slownikKolorow(graf):
    slownik = {}
    for i, kolor in enumerate(graf[2:]):
        slownik[i+1] = kolor
    return slownik

'''
def wiazanieOdWierzcholka(kolory, lista_sasiedztwa, wierzcholek):
    kolor = kolory[wierzcholek]
    wiazanie = set()
    do_odwiedzenia = {wierzcholek}
    while do_odwiedzenia:
        obecny = do_odwiedzenia.pop()
        wiazanie.add(obecny)
        for sasiad in lista_sasiedztwa[obecny - 1][1:]:
            if sasiad not in wiazanie and sasiad not in do_odwiedzenia and kolory[sasiad] == kolor:
                do_odwiedzenia.add(sasiad)
    return wiazanie


def wiazanie(ilosc_wierzcholkow, kolory, lista_sasiedztwa):
    wezly = []
    odwiedzone = set()
    for i in range(1, ilosc_wierzcholkow+1):
        if i not in odwiedzone:
            wynik = wiazanieOdWierzcholka(kolory, lista_sasiedztwa, i)
            odwiedzone = odwiedzone.union(wynik)
            if len(wynik) > 1:
                wezly.append(list(wynik))
    return wezly
'''


def sasiady(ilosc_wierzcholkow, lista_krawedzi):
    lista_sasiedztwa = []
    for i in range(1, ilosc_wierzcholkow+1):
        l3 = []
        l3.append(i)
        for k in lista_krawedzi:
            if k[0] == l3[0]:
                l3.append(k[1])
            elif k[1] == l3[0]:
                l3.append(k[0])
        lista_sasiedztwa.append(l3)

    return lista_sasiedztwa

def dodaj_graf(lista_grafow, nowy_graf):
    nowy_koszt = nowy_graf[0]
    for i, graf in enumerate(lista_grafow):
        koszt = graf[0]
        if nowy_koszt <= koszt:
            lista_grafow = lista_grafow[:i] + [nowy_graf] + lista_grafow[i:]
            return lista_grafow
    return lista_grafow + [nowy_graf]

def selekcja(lista_grafow, populacja):
    # pmax = lista_grafow[0][0]
    # while len(lista_grafow) != populacja:
    #     if len(lista_grafow) == populacja + 1:
    #         c = 1
    #     elif len(lista_grafow) == populacja + 2:
    #         c = 2
    #     indeks4 = int(random.uniform(0, 1) * populacja) + c
    #     prawdopodobienstwo = lista_grafow[indeks4][0]/pmax
    #     if random.uniform(0, 1) < prawdopodobienstwo:
    #         lista_grafow.remove(lista_grafow[indeks4])
        
    return lista_grafow[:populacja]

def wyswietl(lista_grafow):
    print(f'Genetyczny: {int((lista_grafow[0][1])**0.5)} kolorów.')

populacja = 50

lista_grafow = []
for _ in range(populacja):
    losowy_graf = []
    for _ in range(ilosc_wierzcholkow):
        losowy_graf.append(random.randint(1, ilosc))
    losowy_graf = funkcjaKosztu(lista_krawedzi, losowy_graf, False)
    lista_grafow.append(losowy_graf)
lista_grafow.sort()

ilosc_mutacji = 20000

lista_sasiedztwa = sasiady(ilosc_wierzcholkow, lista_krawedzi)
counter = 0
t = False

for _ in range(ilosc_mutacji):
    najlepszy = lista_grafow[0][0]
    if lista_grafow[0][0] == najlepszy:
        counter += 1
        if counter == 5000:
            wyswietl(lista_grafow)
            t = True
            break
    indeks = int(random.uniform(0, 1) * populacja)
    indeks2 = int(random.uniform(0, 1) * populacja)
    while indeks2 == indeks:
        indeks2 = int(random.uniform(0, 1) * populacja)
    rodzic1 = lista_grafow[indeks]
    if lista_grafow[indeks][0] > lista_grafow[indeks2][0]:
        rodzic1 = lista_grafow[indeks2]
    dziecko1 = rodzic1.copy()
    indeks = int(random.uniform(0, 1) * populacja)
    indeks2 = int(random.uniform(0, 1) * populacja)
    rodzic2 = lista_grafow[indeks]
    if lista_grafow[indeks][0] > lista_grafow[indeks2][0]:
        rodzic2 = lista_grafow[indeks2]
    dziecko2 = rodzic2.copy()
    for i in range(ilosc_wierzcholkow//2):
        dziecko1[i+2] = rodzic2[i+2]
        dziecko2[i+2] = rodzic1[i+2]
    dziecko1 = funkcjaKosztu(lista_krawedzi, dziecko1, True)
    dziecko2 = funkcjaKosztu(lista_krawedzi, dziecko2, True)
    lista_grafow = dodaj_graf(lista_grafow, dziecko1)
    lista_grafow = dodaj_graf(lista_grafow, dziecko2)
    indeks3 = int(random.uniform(0, 1) * populacja)
    rodzic3 = lista_grafow[indeks3]
    dziecko3 = rodzic3.copy()
    wierzcholek = int(random.uniform(0, 1) * ilosc_wierzcholkow) + 2
    kolory = jakieKolory(dziecko3)
    koloryRodzica = slownikKolorow(rodzic3)
    for k in lista_sasiedztwa[wierzcholek-2][1:]:
        if koloryRodzica[k] in kolory:
            kolory.remove(koloryRodzica[k])
    if kolory != []:
        dziecko3[wierzcholek] = kolory[0]
    else:
        kolory = jakieKolory(dziecko3)
        dziecko3[wierzcholek] = random.choice(kolory)
    dziecko3 = funkcjaKosztu(lista_krawedzi, dziecko3, True)
    lista_grafow = dodaj_graf(lista_grafow, dziecko3)
    lista_grafow = selekcja(lista_grafow, populacja)

if not t:
    wyswietl(lista_grafow)
    print('Za malo iteracji.')