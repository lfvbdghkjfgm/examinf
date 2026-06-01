# Solved by Анастасия

l = [[int(d) for d in x.split()] for x in open("156")]
ct = 0
for x in l:
    x = sorted(x)
    if x.count(x[0]) == 1:
        if len(set(x)) < 6:
            p = [y for y in x if x.count(y) > 1]
            if (x[0] + x[-1]) < sum(p):
                ct += 1
print(ct)

# Solved by Глеб Г.

l = [[int(d) for d in x.split()] for x in open("31.txt")]
ct = 0
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    povtbol1 = [d for d in x if x.count(d) > 1]
    x = sorted(x)
    if x[0] in povt1 and len(povtbol1) > 0:
        if (x[0] + x[-1]) < sum(povtbol1):
            ct += 1
print(ct)
