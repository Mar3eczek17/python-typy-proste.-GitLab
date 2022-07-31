# Zadanie 1 - Pamiętnik
# Stwórz klasę Pamiętnik, która zaimplementuje metody do odczytywania
# i dopisywania zawartości. Zawartość będzie przechowywana w pliku tekstowym.


class Pamietnik(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def dopisywanie(self, text):
        # Otwarcie pliku do zapisu.
        self.file = open(self.file_name, "a")
        self.file.write(text)
        # Zamknięcie pliku
        self.file.close()

    def odczyt(self):
        # Otwarcie pliku do odczytu.
        self.plik_odczyt = open(self.file_name, 'rt')
        # Odczyt zawartości pliku
        self.caly_tekst = self.plik_odczyt.read()
        self.plik_odczyt.close()
        print(self.caly_tekst)


# Driver code
if __name__ == "__main__":
    nowy = Pamietnik("text.txt")
    # Wywołanie metody dopisywanie do pliku
    nowy.dopisywanie(text="Również dodano ten tekst do zadania\n")
    # Wywołanie metody odczytu z pliku
    nowy.odczyt()
