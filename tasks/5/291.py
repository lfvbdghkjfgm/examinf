# Solved by Илья М.


b = []


def f(m):
    r = ""
    while m > 0:
        r += str(m % 3)
        m //= 3
    return r[::-1]


for N in range(1000):
    g = f(N)
    if (g.count("1") + g.count("2") * 2) % 3 == 0:
        g = "20" + g
    else:
        g = "10" + g
    R = int(g, 3)
    if R < 100:
        print(N)
