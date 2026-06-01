# Solved by Иса

l = [[int(d) for d in x.split()] for x in open("37")]
k = 0
for x in l:
    povt3 = [d for d in x if x.count(d) == 3]
    povt1 = [d for d in x if x.count(d) == 1]
    if len(povt3) == 3 and len(povt1) == 3:
        x = sorted(x)
        if (x[0] ** 2 + x[-1] ** 2) >= (sum(x) - x[0] - x[-1]) ** 2:
            k += 1
print(k)
