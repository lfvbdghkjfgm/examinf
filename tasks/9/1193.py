# Solved by Виктор Г.


t = [[int(d) for d in x.split()] for x in open("9")]
o = 0
for i in t:
    i = sorted(i)
    o += 1
    p = i[0] + i[-1]
    pp = i[1] + i[-2]
    ppp = i[2] + i[-3]
    if len(set(i)) >= 2:
        if p == pp or p == ppp or pp == ppp:
            if (
                p + pp < (sum(i) - (p + pp))
                or p + ppp < (sum(i) - (p + ppp))
                or pp + ppp < (sum(i) - (pp + ppp))
            ):
                print(sum(i), o)
