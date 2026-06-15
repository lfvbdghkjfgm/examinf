# Solved by Владимир Д.


def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0 and x % 10 == 9 and x != 9 and x != d:
            dls.append(x)
        elif d % x == 0 and (d // x) % 10 == 9 and (d // x) != 9 and (d // x) != d:
            dls.append(d // x)

    return sorted(set(dls))


for n in range(800001, 10**8):
    dlss = dels(n)
    if dlss:
        print(n, min(dlss))
