# Solved by Константин Х.


def v3(d):
    s = ""
    while d > 0:
        s += str(d % 3)
        d //= 3
    return s[::-1]


for N in range(1, 1000):
    M = v3(N)
    if sum(map(int, M)) % 3 == 0:
        M = "20" + M
    else:
        M = "10" + M
    R = int(M, 3)
    if R < 100:
        print(N)

# Solved by Глеб Г.


q = []


def f(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for N in range(1, 10000):
    R = f(N)
    if sum(map(int, R)) % 3 == 0:
        R = "20" + R
    else:
        R = "10" + R
    R = int(R, 3)
    if R < 100:
        q.append(N)
print(max(q))
