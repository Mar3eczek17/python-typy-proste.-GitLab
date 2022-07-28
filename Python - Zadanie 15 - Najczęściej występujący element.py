# Zadanie 15.
# Napisz funkcję przyjmujaca jeden parametr list zawierajacy liczby
# całkowite i zwracajaca element, który pojawia się na liscie najczęciej.
def lista(list: list) -> list:
    '''
    Ta funkcja zwraca nam ...
    :param list: list
    :return: list
    '''
    most_common = max(set(list), key=list.count)
    list.append(most_common)
    return list


list = [2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6]
c = lista(list)
print(c)
