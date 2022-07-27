# Zadanie 10.
# Napisz funkcję, która przyjmie dwie listy liczb całkowitych, i zwróci listę liczb
# występujcych w pierwszej i nie występujacych w drugiej liscie,
# posortowana rosnaco względem ilosci wystapien w pierwszej liscie.
def sorted_nums(list_1, list_2):
    c = (set(list_1) - set(list_2))
    d = dict.fromkeys(c, 0)
    for index in list_1:
        if index in c:
            d[index] += 1
    return d


list_1 = [10, 8, 13, 10, 10, 2, 67, 98, 98, -5, 100, 17, 17, 27, 38, 38, 38, 8, 55, 1, 1, 100, 80, 27, 99, 38]
list_2 = [3, 5, 8, 44, 23, 1, -5, 80, 2, 99, 77, 34, 21, 7, 2, 1, 67, 67, 100, 80, 80, 18, 23, 99, 96]
a = sorted_nums(list_1, list_2)
b = sorted(a.items(), key=lambda x: x[1])
print(b)
