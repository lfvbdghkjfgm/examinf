# Solved by Анастасия


import fnmatch


def dels(d):
    s = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            s.append(x)
            s.append(d // x)
    return s


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1


def dels_prime(d):
    s = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0 and is_prime(x):
            s.append(x)
        if d % x == 0 and is_prime(d // x):
            s.append(d // x)
    return s


for x in range(10**6, 1, -1):
    d = dels(x)
    t = dels_prime(x)
    if fnmatch.fnmatch(str(x), "5*") and len(d) == 32:
        print(x, len(t))
