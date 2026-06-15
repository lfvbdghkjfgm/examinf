# Solved by Владимир Д.


def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


ct = 0
for n in range(700_000 + 1, 10**8):
    dls = [d for d in dels(n) if d != 1 and d != n]
    if dls:
        m = max(dls) + min(dls)
    else:
        m = 0

    if str(m)[-1] == "4":
        ct += 1
        print(n, m)

    if ct == 5:
        break
