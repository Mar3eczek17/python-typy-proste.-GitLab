# Zadanie 5.
# Napisz funkcję, która zwróci które urodziny będą obchodziły w tym roku osoby 
# urodzone w latach podanych w lisćie będącej argumentem wejściowym danej 
# funkcji.
def urodziny(x):
    birthday = []
    for i in x:
        item = 2022 - i
        birthday.append(item)
    return birthday

x = [1990, 2000, 1945, 1933, 1987, 1960]
b = urodziny(x)

for x in range(len(b)):
    print(f"W tym roku osoby urodzone w latach podanych w "
          f"licie będącej argumentem wejściowym danej "
          f"funkcji, będą obchodziły: {b[x]} urodziny.")
