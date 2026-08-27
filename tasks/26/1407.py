# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1407_1.txt")
]

data = []

for x in nums:
    id = x[0]
    sm = sum(x[1:])
    pls = sum([i for i in x[1:] if i > 0])
    ct = len([i for i in x[1:] if i != 0])
    if sm > 0:
        data.append([id, sm, pls, ct])

data.sort(key=lambda d: (-d[1], -d[2], -d[3], d[0]))
pr_len = len(data) // 3
prosh = data[:pr_len]
for i in data:
    if i[1:] == prosh[-1][1:] and i not in prosh:
        prosh.append(i)

data = [i for i in data if i not in prosh]

dop_ct = len(data) // 10
dop_otb = data[:dop_ct]
for i in data:
    if i[1:] == dop_otb[-1][1:] and i not in dop_otb:
        dop_otb.append(i)
print(dop_otb[0][0], len(dop_otb))
