# Zadanie 5 - Długość linii prostej
# Stwórz klasę reprezentującą linię prostą, która przyjmuje w konstruktorze współrzędne
# obu końców w układzie współrzędnych XY. Klasa implementuje metodę obliczającą długość linii.
import math


class LiniaProsta(object):
    def __init__(self, krotka):
        self.krotka = krotka

    def line_length(self):
        # Długość odcinka w układzie współrzędnych
        # Długość odcinka o końcach w punktach A=(x1,y1) oraz B=(x2,y2) wyraża się wzorem:
        length_of_the_segment = math.sqrt(pow((self.krotka[2] - self.krotka[0]), 2)
                                          + pow((self.krotka[3] - self.krotka[1]), 2))
        return round(length_of_the_segment, 2)


# Driver code
thistuple = (-3, -2, -11, 4)
d = LiniaProsta(thistuple)
print(f"Długość odcinka o końcach w punktach {d.krotka[0], d.krotka[1]} oraz {d.krotka[2], d.krotka[3]} wynosi: "
      f"{d.line_length()}")
