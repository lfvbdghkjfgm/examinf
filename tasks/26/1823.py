# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

data = [[int(i) for i in x.split()] for x in open("1823_1.txt")]
data = data[1:]
data.sort()

res = [[-1, -1]]

for x in data:
    if x[0] <= res[-1][1] and x[1] > res[-1][1]:
        res[-1][1] = x[1]
    elif x[0] > res[-1][1]:
        res.append(x)
res.append([86400000, 86400002])
sm = 0
for i in range(1, len(res)):
    sm += res[i][0] - res[i - 1][1] - 1

print(len(res) - 1, sm)
