# Solved by Глеб Г.

l = [int(d) for d in open("33.txt")]
q = []
max37 = max([d for d in l if str(d)[-2:] == "37"])
for x in range(len(l) - 3):
    if (
        len(str(l[x])) > 1
        and len(str(l[x + 1])) > 1
        and len(str(l[x + 2])) > 1
        and len(str(l[x + 3])) > 1
    ):
        k = 0
        w = 0
        if l[x] > max37:
            k += 1
        if str(l[x])[-1] == str(l[x])[-2]:
            w += 1
        if l[x + 1] > max37:
            k += 1
        if str(l[x + 1])[-1] == str(l[x + 1])[-2]:
            w += 1
        if l[x + 2] > max37:
            k += 1
        if str(l[x + 2])[-1] == str(l[x + 2])[-2]:
            w += 1
        if l[x + 3] > max37:
            k += 1
        if str(l[x + 3])[-1] == str(l[x + 3])[-2]:
            w += 1
        if k == 2 and w == 1:
            q.append(l[x])
            q.append(l[x + 1])
            q.append(l[x + 2])
            q.append(l[x + 3])
print(len(q) // 4)
summ = 0
for y in q:
    if str(y)[-1] == str(y)[-2]:
        summ += y
print(summ)
