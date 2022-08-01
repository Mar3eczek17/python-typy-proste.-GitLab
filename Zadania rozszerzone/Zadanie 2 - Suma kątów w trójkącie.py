# Zadanie 2 - Suma kątów w trójkącie
# Stwórz klasę Trójkat, w której konstruktor przyjmuje 3 argumenty,
# reprezentujące kąty trójkąta. Klasa implementuje metodę sprawdz_katy,
# która sprawdzi, czy suma kątow jest równa 180.
class Trojkat(object):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def sprawdz_katy(self):
        if ((self.arg1 + self.arg2 + self.arg3 == 180) and self.arg1 != 0 and self.arg2
                != 0 and self.arg3 != 0):
            return True
        else:
            return False


# Driver code
if __name__ == "__main__":
    b = Trojkat(arg1=100, arg2=30, arg3=70)
    print(b.sprawdz_katy().__str__())
