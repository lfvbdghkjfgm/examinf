# Solved by София

l = [[int(d) for d in x.split()] for x in open("1239_1.csv")]
ct = 0
for x in l:
    povt3 = [a for a in x if x.count(a) == 3]
    if len(povt3) == 3 and len(set(x)) == 4:
        if sum(povt3) ** 2 > (sum(x) - sum(povt3)) ** 2:
            ct += 1
print(ct)
