# Zadanie 14.
# Napisz (przy pomocy rekurencji) funkcję realizujaca potęgowanie.
# Funkcja przyjmuje dwie liczby całkowite, będace podstawa i wykładnikiem potęgi.
def potega(a: int, b: int) -> int:
    '''
    Ta funkcja zwraca nam ...
    :param a: int
    :param b: int
    :return: int
    '''
    if b == 0 and a != 0: return 1
    elif (b == 1): return a
    else:
        return (a*potega(a, b - 1))


a = 5
b = 5
c = potega(a, b)
print(c)
