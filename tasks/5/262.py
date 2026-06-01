# Solved by Илья М.

for N in range(1000):
    r = bin(N)[2:]
    g = r.count("1")
    r = r + str(g % 2)
    r = r + str(g % 2)
    R = int(r, 2)
    if R < 86:
        print(N)
