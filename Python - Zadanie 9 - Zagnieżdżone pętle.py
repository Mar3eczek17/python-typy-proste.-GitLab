# Zadanie 9.
# Używajac zagnieżdżonych pętli, stwórz funkcję, która wydrukuje następujcy wzór:
# *
# * $
# * $ *
# * $ * $
# * $ * $ *
# * $ * $
# * $ *
# * $
# *
def wzor():
    for i in range(5):
        for j in range(i + 1):
            print('*' if j % 2 == 0 else '$', end=" ")
        print()

    for i in range(4):
        for j in range(4 - i):
            print('*' if j % 2 == 0 else '$', end=" ")
        print()


z = wzor()
print(type(z))
