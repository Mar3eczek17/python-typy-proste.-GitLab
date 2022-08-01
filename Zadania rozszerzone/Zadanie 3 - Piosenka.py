# Zadanie 3 - Piosenka
# Stwórz klasę przyjmującą w konstruktorze listę będącą kolejnymi wierszami
# piosenki. Klasa będzie mieć metodę spiewaj,
# która wypisze wszystkie wiersze piosenki po kolei.
class Piosenka(object):
    def __init__(self, lista_wierszy):
        self.lista_wierszy = lista_wierszy

    def spiewaj(self):
        for i in self.lista_wierszy:
            print(i)


# Driver code
lista_wierszy = ['Dobrze się pan czuje?',
                 'To świetnie,',
                 'właśnie widzę - jasny wzrok, równy krok',
                 'jak w marszu.',
                 'A ja jestem, proszę pana, na zakręcie.',
                 'Moje prawo to jest pańskie lewo.',
                 'Pan widzi: krzesło, ławkę, stół,',
                 'a ja - rozdarte drzewo.',
                 'Bo ja jestem, proszę pana, na zakręcie.',
                 'Ode mnie widać niebo przekrzywione.',
                 'Pan dzieli każdą zimę, każdy świt na pół.',
                 'Pan kocha swoja żonę.']
b = Piosenka(lista_wierszy)
b.spiewaj()
