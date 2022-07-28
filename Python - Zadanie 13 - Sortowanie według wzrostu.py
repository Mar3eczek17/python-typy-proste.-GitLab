# Zadanie 13.
# Napisz funkcję, która przyjmie słownik mapujacy imiona na wzrost,
# a następnie zwróci listę zawierajaca imiona posortowane według wzrostu malejaco.
def fun(slownik: dict) -> list:
    '''
    Ta funkcja zwraca nam ...
    :param slownik: dict
    :return: list
    '''
    sor_wed_wzrostu = sorted(slownik.items(), key=lambda x: x[1], reverse=True)
    lista = []
    for i in sor_wed_wzrostu:
        lista.append(i[0])
    return lista


slownik = {'Marek': 177, 'Tomek': 185, 'Maciek': 170, 'Krystian': 178, 'Karol': 180}
b = fun(slownik)
print(b)
