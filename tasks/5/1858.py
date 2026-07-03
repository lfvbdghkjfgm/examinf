# Solved by София


def f3(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


d = []
for n in range(167, 1000):
    r = f3(n)
    if sum(map(int, str(r))) % 9 == 0:
        r += "2"
    else:
        r += f3(sum(map(int, str(r))) % 9)
    r = int(r, 3)
    d.append(r)
print(min(d))

# Solved by Аня


s = []


def v3(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for N in range(1, 1000):
    r = v3(N)
    if sum(map(int, r)) % 9 == 0:
        r = r + "2"
    else:
        r = r + v3((sum(map(int, r))) % 9)
    r = int(r, 3)
    if N > 166:
        s.append(r)
print(min(s))
