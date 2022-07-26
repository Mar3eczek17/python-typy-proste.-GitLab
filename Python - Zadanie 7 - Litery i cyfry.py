# Napisz funkcję przyjmujacą napis i zwracającą informacje ile liter i cyfr jest w napisie.
def intersection(napis):
    numbers = sum(c.isdigit() for c in napis)
    letters = sum(c.isalpha() for c in napis)
    return numbers, letters


napis = 'ajnfjaafo2912euri1r910r9jr01r1'
z = intersection(napis)
print(f"W napisie zawiera się {z[1]} liter i {z[0]} cyfr.")
