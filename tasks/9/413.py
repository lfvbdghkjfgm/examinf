# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in j.split(";")] for j in open("413_1.csv")]
res = 0
for x in nums:
    a = [max(x), min(x)]
    if not x[0] in a and not x[-1] in a and x[0] != x[-1]:
        if not (a[0] - a[1]) % (x[0] - x[-1]):
            res += 1
print(res)

# Solved by Мария


l = [[int(d) for d in x.split()] for x in open("4.txt")]
ct = 0
for x in l:
    if x[0] != min(x) and x[0] != max(x) and x[-1] != min(x) and x[-1] != max(x):
        y = sorted(x)
        if y[2] != y[1] and (y[-1] - y[0]) % (y[2] - y[1]) == 0:
            ct += 1
print(ct)
