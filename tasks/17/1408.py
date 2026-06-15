# Solved by Владимир Д.


l = [int(x) for x in open("other/examinf/17/1408.txt")]
min_17 = min([x for x in l if x % 17 == 0 and len(str(abs(x))) == 4]) ** 2

ct = 0
mnsm = float("inf")

for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    usl1 = [x for x in (a, b, c) if len(str(abs(x))) == 4 and abs(x) % 100 == 27]
    if usl1:
        sm = a**2 + b**2 + c**2
        if sm <= min_17:
            ct += 1
            mnsm = min(mnsm, (abs(a) + abs(b) + abs(c)))


print(ct, mnsm)
