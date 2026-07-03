# Solved by Иса


m = []
for n in range(1, 10000):
    r = bin(n)[2:]
    if sum(map(int, str(n))) % 2 == 0:
        r += "0"
    else:
        r += "1"
    if sum(map(int, str(n))) % 2 == 0:
        r += "0"
    else:
        r += "1"
    if sum(map(int, str(n))) % 2 == 0:
        r += "0"
    else:
        r += "1"
    r = int(r, 2)
    if r > 2064:
        m.append(r)
print(min(m))
