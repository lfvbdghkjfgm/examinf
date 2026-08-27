# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1700_1.txt")]

res = []

for i in range(len(nums) - 2):
    l = nums[i : i + 3]
    c1 = [i for i in l if str(i)[0] == str(i)[-1]]
    c2 = [i for i in l if len(str(i)) == 4 and str(i)[1] == "2"]
    if len(c1) == 1 and len(c2) == 2:
        res.append(max(l))

print(len(res), sum(res))

# Solved by Вадим С.


l = [int(x) for x in open("1700_1.txt")]
c = []
for x in range(len(l) - 2):
    t = [l[x], l[x + 1], l[x + 2]]
    h = [i for i in t if str(i)[0] == str(i)[-1]]
    g = [i for i in t if len(str(i)) == 4 and str(i)[1] == "2"]
    if len(h) == 1 and len(g) == 2:
        c.append(max(t))
print(len(c), sum(c))

# Solved by Владимир Д.


l = [int(x) for x in open("examinf/17/1700.txt")]

ct = 0
mxsm = []
for i in range(len(l) - 2):
    a, b, c = l[i], l[i + 1], l[i + 2]
    usl1 = [d for d in (a, b, c) if str(d)[0] == str(d)[-1]]
    if len(usl1) == 1:
        usl2 = [d for d in (a, b, c) if len(str(d)) == 4 and str(d)[-3] == "2"]
        if len(usl2) == 2:
            ct += 1
            mxsm.append(max(a, b, c))

print(ct, sum(mxsm))
