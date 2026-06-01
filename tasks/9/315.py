# Solved by Глеб Г.

l = [[int(d) for d in x.split()] for x in open("32.txt")]
ct = 0
for x in l:
    x = sorted(x)
    if (x[0] ** 2 + x[1] ** 2) == x[-1] ** 2:
        ct += 1
print(ct)
