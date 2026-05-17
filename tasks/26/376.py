# Solved by lfvbdghkjfgm
# https://lfvb.ru

k = 8
data = [[int(i) for i in x.split()] for x in open("1.txt")]
data.sort()
data = [[a, a + b] for a, b in data]
res = [data[0]]

for a, b in data[1:]:
    if a >= res[-1][0] and b < res[-1][1]:
        res[-1] = [a, b]
    elif a >= res[-1][1]:
        res.append([a, b])
r1 = 0
for a, b in data:
    if a > res[-2][1]:
        r1 = a
        break
print(len(res) * k, r1)
