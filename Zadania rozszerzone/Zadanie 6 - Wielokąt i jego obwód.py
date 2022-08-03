# Zadanie 6 - Wielokąt i jego obwód
# Stwórz klasę reprezentującą wielokąt i przyjmującą w konstruktorze listę kolejnych linii
# (obiekty klasy z poprzedniego zadania), reprezentujących kolejne boki wielokąta. Klasa powinna sprawdzić,
# czy dane są poprawne (czy każda linia kończy się tam, gdzie zaczyna następna). Klasa wielokąta implementuje
# również metodę obliczającą obwód.

import itertools
import math


class Polygon(object):
    def __init__(self, lista_linii):
        self.lista_linii = lista_linii

    # Sprawdzenie, czy dane są poprawne (czy każda linia kończy się tam, gdzie zaczyna następna).
    # Kod 1
    def sprawdzenie(self):
        for i in range(len(self.lista_linii)):
            # Z założeniem, że linie są zawsze posortowane
            # range(len(self.lista_linii)) -> taki zapis przechowuje w pamięci podrzędną wartość,
            # a to jest nam niezbędne do sprawdzenia
            if self.lista_linii[i][0] != self.lista_linii[i - 1][1]:
                return False
            return True

    # enumerate również tutaj zadziała
    # Kod 2 -> Enumerate
    # def sprawdzenie(self):
    #     for i, j in enumerate(self.lista_linii):
    #         if self.lista_linii[i][0] != self.lista_linii[i - 1][1]:
    #             return False
    #         return True

    # Kod 3
    # def sprawdzenie(self):
    #     for first, second in zip(self.lista_linii, self.lista_linii[1:]):
    #         if first[1] != second[0]:
    #             return False
    #     if self.lista_linii[0][0] != self.lista_linii[-1][1]:
    #         return False
    #     return True

    def circuit(self):
        # Kod 1
        # res = list(itertools.chain.from_iterable(self.lista_linii))
        # print(res)
        # Kod 2 równoważny z Kodem 1
        res = [a for tup in self.lista_linii for a in tup]
        # Rozpakowanie zagnieżdżonej listy
        wsp = [j for i in res for j in i]
        wsp_t = tuple(wsp)
        print(wsp_t)

        lista = []
        for j in range(len(wsp_t)):
            if j % 4 == 0:
                length = math.sqrt(pow((wsp_t[j + 2] - wsp_t[j]), 2) + pow((wsp_t[j + 3] - wsp_t[j + 1]), 2))

                lista.append(length)
                j += 1
        print(f"Obwód wielokąta równa się: {round(sum(lista), 3)} w zaokrągleniu do 3 miejsca po przecinku.")


# Driver code
obiekt = [([3, 4], [5, 6]), ([5, 6], [8, 2]), ([8, 2], [5, 0]), ([5, 0], [3, 4])]
d = Polygon(obiekt)
print(d.sprawdzenie())
d.circuit()
