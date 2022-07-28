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
    [zaludnienie.append(x['liczba_mieszkancow']) for x in lista_slownikow]
    [powierzchnia.append(x['powierzchnia']) for x in lista_slownikow]

    # Inny sposób na dodanie gęstości zaludnienia...
    for panstwo in lista_slownikow:
        panstwo['gestosc_zaludnienia'] = round(panstwo['liczba_mieszkancow'] / panstwo['powierzchnia'], 2)
    print(lista_slownikow)

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
d = panstwa(a, arg1='gestosc_zaludnienia')
#       PKB per capita (PPP)
# e = panstwa(a, arg1='PKB_per_capita_PPP')
# print(b)
# print(c)
print(d)
# print(e)
