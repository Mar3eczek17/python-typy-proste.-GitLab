# Zadanie 12.
# Napisz funkcję, która przyjmie argumenty nazwane imie i wzrost a następnie
# utworzy wpis do globalnego słownika. Dodaj co najmniej 5 wpisów.

globalny_slownik = {}


def slownik(imie: str, wzrost: int) -> dict:
    '''
    Ta funkcja zwraca nam ...
    :param imie: str
    :param wzrost: int
    :return: globalny_slownik: dict
    '''
    global globalny_slownik
    globalny_slownik[imie] = wzrost
    return globalny_slownik


# Driver code
print('EmptyGlobalDict', globalny_slownik)

slownik(imie='Marek', wzrost=177)
print('NewGlobalDict, 1wpis', globalny_slownik)
slownik(imie='Tomek', wzrost=185)
print('NewGlobalDict, 2wpis', globalny_slownik)
slownik(imie='Maciek', wzrost=170)
print('NewGlobalDict, 3wpis', globalny_slownik)
slownik(imie='Krystian', wzrost=178)
print('NewGlobalDict, 4wpis', globalny_slownik)
slownik(imie='Karol', wzrost=180)
print('NewGlobalDict, 5wpis', globalny_slownik)
