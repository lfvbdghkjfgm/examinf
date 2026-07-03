# Solved by Анастасия


def v3(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


d = []
for n in range(1, 1000):
    r = v3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += v3(sum(map(int, r)))
    r = int(r, 3)
    if r % 2 != 0 and r > 278:
        d.append(r)
print(min(d))

# Solved by Глеб Г.


l = []


def f(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for N in range(1, 10000):
    R = f(N)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + f(sum(map(int, R)))
    R = int(R, 3)
    if R > 278 and int(R) % 2 != 0:
        l.append(R)
print(min(l))
