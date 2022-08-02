# Zadanie 5 - Długość linii prostej
# Stwórz klasę reprezentującą linię prostą, która przyjmuje w konstruktorze współrzędne
# obu końców w układzie współrzędnych XY. Klasa implementuje metodę obliczającą długość linii.
import math


class LiniaProsta(object):
    def __init__(self, pkt_a, pkt_b):
        self.pkt_a = pkt_a
        self.pkt_b = pkt_b
        self.pkt_c = [pkt_b[0], pkt_a[1]]

    def line_length(self):
        # Długość odcinka w układzie współrzędnych
        # Długość odcinka o końcach w punktach A=(x1,y1) oraz B=(x2,y2) wyraża się wzorem:
        length_of_the_segment = math.sqrt(pow((self.pkt_b[0] - self.pkt_a[0]), 2)
                                          + pow((self.pkt_b[1] - self.pkt_a[1]), 2))
        return round(length_of_the_segment, 2)


# Driver code
d = LiniaProsta([-3, -2], [-11, 4])
print(d.pkt_a)
print(d.pkt_b)
print(f"Długość odcinka o końcach w punktach {d.pkt_a} oraz {d.pkt_b} wynosi: {d.line_length()}")
print(d.line_length())
