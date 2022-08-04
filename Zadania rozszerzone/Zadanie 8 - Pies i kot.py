# Zadanie 8 - Pies i kot
# Stwórz klasy potomne dla klasy bazowej zwierzęcia, reprezentujące psa i kota.
# W konstruktorze każdej z nich ustaw odpowiednio zmienną reprezentującą typ zwierzęcia.
# Zaimplementuj odpowiednio metodę daj_głos w każdej z klas potomnych.
# Sprawdź, czy obiekty stworzone z klas Pies i Kot potrafią poprawnie się przywitać.
class Animals:
    def __init__(self, typ):
        self.typ = typ


class Dog(Animals):
    def daj_glos(self):
        return f"Cześć jestem: {self.typ}"


class Cat(Animals):
    def daj_glos(self):
        return f"Cześć jestem: {self.typ}"


bark = Dog('husky')
print(bark.daj_glos())
meow = Cat('perski')
print(meow.daj_glos())
