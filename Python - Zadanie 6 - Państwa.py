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

# Zadanie 6.
# Wybierz kilka państw i stwórz dla każdego słownik, który będzie zawierać dane o nazwie
# państwa, powierzchni, liczbie mieszkańców, PKB per capita (PPP). Napisz funkcję,
# która dla listy słowników będzie wypisywać listę państw uszeregowanych według:

# Arkadiusz Modzelewski
# Z gęstością jest ok, ale zarówno gęstość jak i sortowanie powinno odbywać
# się w funkcji. Potrzebna jest tylko i wyłącznie jedna funkcja, która będzie pobierać listę
# państw, o których dane są w słownikach. Potem wewnątrz tej funkcji dopisujesz do słownika
# gęstość do każdego państwa i potem sortujesz na podstawie argumentu, który przekażesz do
# funkcji np pozadkowanie(lista_panstw, "powierzchnia") - takie wywolanie funkcji powinno
# posortować słowniki po powierzchni i zwrócić listę państwa z samymi nazwami, ale juz
# posortowanymi.

# Piotr Glinka
# napisałeś kilka funkcji porządkujących, każda dla innego klucza - napisz funkcję która
# ten klucz przekaże jako parametr 🙂

# poprawka
def panstwa(lista_slownikow: list, arg1: str) -> list:
    '''
    Ta funkcja zwraca nam ...
    :param lista_slownikow: list
    :param arg1: str
    :return: list
    '''
    zaludnienie = []
    powierzchnia = []
    gestosc_zaludnienia = []
    [zaludnienie.append(x['liczba_mieszkancow']) for x in lista_slownikow]
    [powierzchnia.append(x['powierzchnia']) for x in lista_slownikow]

    for i in range(len(zaludnienie)):
        gestosc_zaludnienia.append(zaludnienie[i] / powierzchnia[i])

    Panstwo1['gestosc_zaludnienia'] = round(gestosc_zaludnienia[0], 2)
    Panstwo2['gestosc_zaludnienia'] = round(gestosc_zaludnienia[1], 2)
    Panstwo3['gestosc_zaludnienia'] = round(gestosc_zaludnienia[2], 2)
    Panstwo4['gestosc_zaludnienia'] = round(gestosc_zaludnienia[3], 2)

    newlist = sorted(lista_slownikow, key=lambda d: d[arg1])

    lista_panstw = []
    for x in newlist:
        lista_panstw.append(x['nazwa'])
    return lista_panstw


# Driver code - parametry funkcji uruchamia się przez odkomentowanie
# parametrów, które chcemy użyć i zakomentowanie, już użytych...
lista_slownikow = [Panstwo1, Panstwo2, Panstwo3, Panstwo4]
a = lista_slownikow
#       powierzchni
# b = panstwa(a, arg1='powierzchnia')
#       liczby ludności
# c = panstwa(a, arg1='liczba_mieszkancow')
#       gęstości zaludnienia
# d = panstwa(a, arg1='gestosc_zaludnienia')
#       PKB per capita (PPP)
e = panstwa(a, arg1='PKB_per_capita_PPP')
# print(b)
# print(c)
# print(d)
print(e)
