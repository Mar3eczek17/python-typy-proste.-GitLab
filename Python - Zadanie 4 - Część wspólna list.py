# Zadanie 4.
# Napisz funkcję, która dla dwóch list liczbowych zwróci listę zawierającą 
# tylko te elementy, które należą do obydwu list wejściowych.
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
 
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [69, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))
