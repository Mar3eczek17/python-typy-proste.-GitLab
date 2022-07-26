Panstwo1 = {'nazwa': 'Niemcy',
               'powierzchnia': 357588,
               'liczba_mieszkancow': 83240000,
               'PKB_per_capita_PPP': 55220}

Panstwo2 = {'nazwa': 'Polska',
               'powierzchnia': 322575,
               'liczba_mieszkancow': 37950000,
               'PKB_per_capita_PPP': 33220}

Panstwo3 = {'nazwa': 'Holandia',
               'powierzchnia': 41543,
               'liczba_mieszkancow': 17740000,
               'PKB_per_capita_PPP': 59700}

Panstwo4 = {'nazwa': 'Anglia',
               'powierzchnia': 243610,
               'liczba_mieszkancow': 55980000,
               'PKB_per_capita_PPP': 47620}

lista_slownikow = [Panstwo1, Panstwo2, Panstwo3, Panstwo4]

# Zadanie 6.
# Wybierz kilka państw i stwórz dla każdego słownik, który będzie zawierać dane o nazwie
# państwa, powierzchni, liczbie mieszkańców, PKB per capita (PPP). Napisz funkcję,
# która dla listy słowników będzie wypisywać listę państw uszeregowanych według:

zaludnienie = []
powierzchnia = []
gestosc_zaludnienia = []
y = [zaludnienie.append(x['liczba_mieszkancow']) for x in lista_slownikow]
z = [powierzchnia.append(x['powierzchnia']) for x in lista_slownikow]

for i in range(len(zaludnienie)):
    gestosc_zaludnienia.append(zaludnienie[i]/powierzchnia[i])
# print(gestosc_zaludnienia)

Panstwo1['gestosc_zaludnienia'] = gestosc_zaludnienia[0]
Panstwo2['gestosc_zaludnienia'] = gestosc_zaludnienia[1]
Panstwo3['gestosc_zaludnienia'] = gestosc_zaludnienia[2]
Panstwo4['gestosc_zaludnienia'] = gestosc_zaludnienia[3]


#       powierzchni
newlist = sorted(lista_slownikow, key=lambda d: d['powierzchnia'])

def pozadkowanie(newlist):
    lista_panstw = []
    for x in newlist:
        lista_panstw.append(x['nazwa'])
    return lista_panstw

z = pozadkowanie(newlist)
print(z)

#       liczby ludności
newlist1 = sorted(lista_slownikow, key=lambda d: d['liczba_mieszkancow'])

def pozadkowanie(newlist1):
    lista_panstw = []
    for x in newlist1:
        lista_panstw.append(x['nazwa'])
    return lista_panstw

z = pozadkowanie(newlist1)
print(z)

#       gęstości zaludnienia
newlist2 = sorted(lista_slownikow, key=lambda d: d['gestosc_zaludnienia'])

def pozadkowanie(newlist2):
    lista_panstw = []
    for x in newlist2:
        lista_panstw.append(x['nazwa'])
    return lista_panstw

z = pozadkowanie(newlist2)
print(z)

#       PKB per capita (PPP)
newlist3 = sorted(lista_slownikow, key=lambda d: d['PKB_per_capita_PPP'])

def pozadkowanie(newlist3):
    lista_panstw = []
    for x in newlist3:
        lista_panstw.append(x['nazwa'])
    return lista_panstw

z = pozadkowanie(newlist3)
print(z)
