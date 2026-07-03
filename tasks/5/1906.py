# Solved by Аня


for n in range(1, 10000):
    r = bin(n)[2:]
    if n % 4 == 0:
        r = r + r[0:3]
    else:
        r = r + bin((n % 4) + 1)[2:]
    r = int(r, 2)
    if r >= 50:
        print(n)
