# Zadanie 11.
# Utworz funkcję, która przyjmie argument int n i obliczy n-ta liczbę ciagu
# Fibonacciego.
def fib(n: int) -> int:
    '''
    Ta funkcja zwraca nam ...
    :param n: int
    :return: fib(n - 1) + fib(n - 2): int
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# Driver code
n = 9
b = fib(n)
print(b)
