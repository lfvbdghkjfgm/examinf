# Solved by Владимир Д.


l = [int(x) for x in open("other/examinf/17/944.txt")]
mx8 = max([x for x in l if str(abs(x))[0] == "8"])
ct = 0
mnsm = float("inf")
for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    usl1 = [d for d in (a, b, c) if str(abs(d))[0] == "6"]
    if len(usl1) <= 1:
        sm = a + b + c
        if sm >= mx8:
            ct += 1
            mnsm = min(mnsm, sm)

print(ct, mnsm)
