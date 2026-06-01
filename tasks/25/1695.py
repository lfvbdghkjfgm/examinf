# Solved by lfvbdghkjfgm
# https://lfvb.ru


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return sorted(list(res))


k = 0
for i in range(1_350_051, 10**10):
    d = dels(i)
    t = [j for j in d if j % 100 == 11 and j not in [i, 11]]
    if t:
        print(i, min(t))
        k += 1
    if k == 5:
        break
