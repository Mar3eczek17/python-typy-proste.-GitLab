# Zadanie 7 - Zwierzęta
# Stwórz abstrakcyjną klasę bazową reprezentującą zwierzę. Konstruktor klasy będzie przyjmować
# parametr reprezentujący imię zwierzęcia. Klasa będzie mieć 2 metody. Jedna metoda daj_glos
# będzie abstrakcyjna. Druga metoda powitanie będzie wyświetlać napis, składający się
# z wartości zwracanej przez daj_glos, z wyświetlenia imienia zwierzęcia oraz z wyświetlenia
# jakiego typu (atrybut typ dla klasy) jest zwierzę.
from abc import abstractmethod


class Zwierze:
    def __init__(self, imie, typ):
        self.imie = imie
        self.typ = typ

    @abstractmethod  # tutaj wymuszamy implementację tej metody w klasach pochodnych
    def daj_glos(self):
        return "Ihhhhiiiii!"

    def powitanie(self):
        return f"{self.daj_glos()}. Mam na imię: {self.imie}, i jestem {self.typ}."


obiekt = Zwierze('Kary', 'Koniem')
print(obiekt.powitanie())
