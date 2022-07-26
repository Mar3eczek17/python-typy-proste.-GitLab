# Zadanie 8.
# Napisz funkcję, która sprawdzi czy 2 napisy sa palindromami.

def isPalindrome(s, z):
    if s == z[::-1]:
        return True
    else:
        return False


# Driver code
s = "zakaz"
z = "zakaz"
ans = isPalindrome(s, z)

if ans:
    print("Yes")
else:
    print("No")
