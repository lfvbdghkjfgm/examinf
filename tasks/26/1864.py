# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\1864_1.txt")]

n = data[0][0]
data = sorted(data[1:])

res = [[-2, -2]]

for i in range(365):
    ct = 0
    for start, end in data:
        if start <= i <= end:
            ct += 1
    if ct == n:
        if i - res[-1][1] == 1:
            res[-1][1] += 1
        else:
            res.append([i, i])
res = res[1:]

print(len(res), max([end - start + 1 for start, end in res]))
