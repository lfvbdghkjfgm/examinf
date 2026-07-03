# Solved by Влад


a = []


def f(n):
    s = ""
    while n:
        s += str(n % 4)
        n //= 4
    return s[::-1]


for n in range(1, 1000):
    t = f(n)
    if (
        t.count("2")
        + t.count("4")
        + t.count("6")
        + t.count("8")
        + t.count("0")
        + t.count("1")
        + t.count("3")
        + t.count("5")
        + t.count("7")
        + t.count("9")
    ) % 2 == 0:
        t = t[: len(t) // 2] + "0" + t[len(t) // 2 :]
    else:
        t = t
    r = int(t)
    if r <= 180:
        a.append(n)
print(max(a))

# Solved by Виктор Г.


def f(x):
    r = ""
    while x > 0:
        r += str(x % 4)
        x //= 4
    return r[::-1]


for n in range(100000):
    t = f(n)
    if len(t) % 2 == 0:
        q = len(str(t)) // 2
        t = t[:q] + "0" + t[q:]
    else:
        t = t
    t = int(t)
    if t <= 180:
        print(n)

# Solved by Илья М.


b = []


def f(m):
    r = ""
    while m > 0:
        r += str(m % 4)
        m //= 4
    return r[::-1]


for N in range(1000):
    g = f(N)
    if len(g) % 2 == 0:
        g = g[:2] + "0" + g[2:]
    R = int(g)
    if R <= 180:
        print(N)
