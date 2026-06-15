# Solved by Аня


import fnmatch


def dels(d):
    l = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0 and fnmatch.fnmatch(str(x), "2*3?"):
            l.append(x)
        if d % x == 0 and fnmatch.fnmatch(str(d // x), "2*3?"):
            l.append(d // x)
    return sorted(set(l))


for y in range(500_001, 3_000_000):
    m = dels(y)
    if len(m) > 0:
        print(y, min(m))
