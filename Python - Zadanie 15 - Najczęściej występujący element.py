# Zadanie 15.
# Napisz funkcję przyjmujaca jeden parametr list zawierajacy liczby
# całkowite i zwracajaca element, który pojawia się na liscie najczęciej.

def najczestszy_element(lista_liczb: list) -> int:
    '''
    Ta funkcja zwraca nam ...
    :param lista_liczb: list
    :return: int
    '''
    most_common = max(lista_liczb, key=lista_liczb.count)
    return most_common


lista_liczb = [1, 2, 3, 6, 3, 6, 6, 3, 6, 5, 5, 6, 7, 1, 7, 2, 1, 1, 7, 1, 1]
c = najczestszy_element(lista_liczb)
print(c)
