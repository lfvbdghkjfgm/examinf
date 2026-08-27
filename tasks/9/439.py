# Solved by Виктор Г.


t = [[int(d) for d in x.split()] for x in open("9")]
o = []
for i in t:
    k = [int(d) for d in i if i.count(d) == 3]
    s = [int(d) for d in i if i.count(d) == 2]
    if len(set(k)) == 1 and len(set(s)) == 2:
        i = sorted(i)
        c = [i[d] for d in range(4)]
        if (c[0] + c[-1]) % 2 != 0 and (c[1] + c[2]) % 2 != 0:
            o.append(sum(i))
print(sum(o))
