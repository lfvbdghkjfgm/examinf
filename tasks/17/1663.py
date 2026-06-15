# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [int(i) for i in open(r"C:\Users\111\Downloads\1663_1.txt")]

res = 0
sm = 0

for i in range(len(nums) - 2):
    l = nums[i : i + 3]
    c1 = [i for i in l if i % 40 == 15]
    c2 = [i for i in l if i % 7 == 0]
    if len(c1) == 2 and len(c2) <= 2:
        res += 1
        sm += sum([i for i in l if i % 40 != 15])


print(res, sm)

# Solved by Данзан С.


l = [int(x) for x in open("41.txt")]
ost15 = []
kol = 0
for x in range(len(l) - 2):
    k = 0
    if l[x] % 40 == 15:
        k += 1
    if l[x + 1] % 40 == 15:
        k += 1
    if l[x + 2] % 40 == 15:
        k += 1
    if k == 2:
        ct = 0
        if l[x] % 7 == 0:
            ct += 1
        if l[x + 1] % 7 == 0:
            ct += 1
        if l[x + 2] % 7 == 0:
            ct += 1
        if ct <= 2:
            kol += 1
            if l[x] % 40 != 15:
                ost15.append(l[x])
            if l[x + 1] % 40 != 15:
                ost15.append(l[x + 1])
            if l[x + 2] % 40 != 15:
                ost15.append(l[x + 2])
print(kol, sum(ost15))
