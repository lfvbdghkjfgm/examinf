# Solved by lfvbdghkjfgm
# https://lfvb.ru


def dels(num):
    res = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return sorted(list(res))


k = 1
for i in range(201455, 201470):
    t = dels(i)
    if len(t) == 4:
        print(*t)
