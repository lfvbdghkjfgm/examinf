# Solved by София


def f5(n):
    s = ""
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s


a = 7 * 5**1984 - 6 * 25**777 + 5 * 125**333 - 4
b = f5(a)
print(sum(map(int, str(b))))
