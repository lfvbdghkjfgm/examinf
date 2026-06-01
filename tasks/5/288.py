# Solved by Влад

a = []


def f(n):
    s = ""
    while n:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for n in range(11, 1000):
    t = f(n)
    if (t.count("2") + t.count("4") + t.count("6") + t.count("8") + t.count("0")) > (
        t.count("1") + t.count("3") + t.count("5") + t.count("7") + t.count("9")
    ):
        t = "22" + t
    else:
        t = "11" + t
    r = int(t, 3)
    if r > 100:
        a.append(r)
print(min(a))

# Solved by Илья М.

b = []


def f(m):
    r = ""
    while m > 0:
        r += str(m % 3)
        m //= 3
    return r[::-1]


for N in range(11, 1000):
    g = f(N)
    if (g.count("0") + g.count("2")) > g.count("1"):
        g = "22" + g
    else:
        g = "11" + g
    R = int(g, 3)
    if R > 100:
        b.append(R)
print(min(b))
