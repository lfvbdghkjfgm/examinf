# Solved by Константин Х.


l = [int(x) for x in open("15.txt")]
srar = sum([d for d in l]) / len(l)
mn = []
for x in range(len(l) - 1):
    if l[x] < srar or l[x + 1] < srar:
        k = 0
        if l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0:
            k += 1
        if (
            l[x + 1] % 7 == 0
            and l[x + 1] % 3 != 0
            and l[x + 1] % 11 != 0
            and l[x + 1] % 13 != 0
        ):
            k += 1
        if k >= 1:
            mn.append(l[x] + l[x + 1])
print(len(mn), min(mn))

# Solved by Глеб Г.


l = [int(d) for d in open("37.txt")]
q = []
sraf = sum(l) / len(l)
for x in range(len(l) - 1):
    k = 0
    w = 0
    if l[x] < sraf:
        k += 1
    if l[x + 1] < sraf:
        k += 1
    if l[x] % 7 == 0 and l[x] % 3 != 0 and l[x] % 11 != 0 and l[x] % 13 != 0:
        w += 1
    if (
        l[x + 1] % 7 == 0
        and l[x + 1] % 3 != 0
        and l[x + 1] % 11 != 0
        and l[x + 1] % 13 != 0
    ):
        w += 1
    if k > 0 and w > 0:
        q.append(l[x] + l[x + 1])
print(len(q), min(q))
