# Solved by Аня


l = [int(x) for x in open("bite1.17.txt")]
mx = max([x for x in l if len(str(x)) == 3])
sp = []
for x in range(len(l) - 1):
    k = 0
    if len(str(l[x])) == 3:
        k += 1
    if len(str(l[x + 1])) == 3:
        k += 1
    if k == 1:
        if (l[x] * l[x + 1]) % mx == 0:
            sp.append(l[x] * l[x + 1])
print(len(sp), min(sp))
