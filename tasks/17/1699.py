# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import prod

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1699_1.txt")]

res = []
mx = max(nums)

for i in range(len(nums) - 2):
    l = nums[i : i + 3]
    minus = [i for i in l if i < 0] + [0]
    plus = [i for i in l if i > 0] + [0]
    if abs(sum(minus)) <= sum(plus) and str(prod(l))[-1] == str(mx)[-1]:
        res.append(abs(prod(l)))

print(len(res), max(res))

# Solved by Глеб Г.


l = [int(d) for d in open("34.txt")]
w = []
mx = max(l)
for x in range(len(l) - 2):
    q = []
    q.append(l[x])
    q.append(l[x + 1])
    q.append(l[x + 2])
    otric = [d for d in q if d < 0]
    poloz = [d for d in q if d > 0]
    if abs(sum(otric)) <= sum(poloz):
        if str(l[x] * l[x + 1] * l[x + 2])[-1] == str(mx)[-1]:
            w.append(abs(l[x] * l[x + 1] * l[x + 2]))
print(len(w), max(w))

# Solved by Владимир Д.


from math import prod

l = [int(x) for x in open("other/examinf/17/1699.txt")]
mx = max(l)
ct = 0
mxpr = -float("inf")
for x in range(len(l) - 2):
    a, b, c = l[x], l[x + 1], l[x + 2]
    ng_sm = abs(sum([d for d in (a, b, c) if d < 0]))
    ps_sm = abs(sum([d for d in (a, b, c) if d > 0]))
    if ng_sm <= ps_sm:
        if abs(prod((a, b, c))) % 10 == abs(mx) % 10:
            ct += 1
            mxpr = max(mxpr, abs(prod((a, b, c))))

print(ct, mxpr)
