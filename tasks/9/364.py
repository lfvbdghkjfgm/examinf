# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [[int(i) for i in j.split(";")] for j in open("364_1.csv")]
res = 0
for x in nums:
    d = [i for i in x if not i % 3]
    if len(d) == 3 and (max(x) - min(x)) <= sum(d):
        res += 1
print(res)

# Solved by Глеб Г.


l = [[int(d) for d in x.split()] for x in open("1.txt")]
ct = 0
for x in l:
    kr3 = [d for d in x if d % 3 == 0]
    if max(x) - min(x) <= sum(kr3) and len(kr3) == 3:
        ct += 1
print(ct)

# Solved by София


l = [[int(d) for d in x.split()] for x in open("364_1.csv")]
ct = 0
for x in l:
    kra = [a for a in x if a % 3 == 0]
    if len(kra) == 3:
        x = sorted(x)
        if x[-1] - x[0] <= sum(kra):
            ct += 1
            print(x)
print(ct)
