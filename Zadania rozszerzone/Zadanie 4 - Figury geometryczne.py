# Zadanie 4 - Figury geometryczne
# Zaimplementuj klasę bazową Figura. Klasa będzie mieć metody obliczające pole i obwod. 
# Stwórz klasy reprezentujące trójkąt i prostokąt, implementujące odpowiednio obie metody.
class Figura:
    def __init__(self, a_troj, h_troj, b_troj, c_troj, a_pros, b_pros):
        self.a_troj = a_troj
        self.h_troj = h_troj
        self.b_troj = b_troj
        self.c_troj = c_troj
        self.a_pros = a_pros
        self.b_pros = b_pros

    def pole(self):
        pass

    def obwod(self):
        pass


class Prostokat(Figura):
    def R_area(self):
        a = self.a_pros * self.b_pros
        print("Area of Rectengular", "is", a)

    def R_circuit(self):
        a = 2 * (self.a_pros + self.b_pros)
        print("Circuit of Rectengular", "is", a)


class Trojkat(Figura):
    def T_area(self):
        a = 0.5 * self.a_troj * self.h_troj
        print("Area of Triangle", "is", a)

    def T_circuit(self):
        a = self.a_troj + self.b_troj + self.c_troj
        print("Circuit of Triangle", "is", a)


# Driver code
obr = Prostokat(6, 5, 8, 4, 5, 10)
obr.R_area()
obr.R_circuit()
print('----------------------------')
obs = Trojkat(5, 10, 10, 20, 8, 6)
obs.T_area()
obs.T_circuit()
