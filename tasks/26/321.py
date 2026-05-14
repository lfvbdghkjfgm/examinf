# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [i.split() for i in open("1.txt")]
data = [[int(a), int(b), c[1:]] for a, b, c in data]

picksels = {}
res = {}

for a in range(1, 10_000):
    picksels[a] = [""] * 10_000
    res[a] = 0

for a, b, c in data:
    picksels[a][b - 1] = c

for a, b in picksels.items():
    if b.count("0000FF") < 6:
        continue
    for i in range(len(b)):
        if (
            i >= 3
            and b[i] == "00FF00"
            and all([b[i - j] == "0000FF" for j in range(-3, 0)])
            and all([b[i - j] == "0000FF" for j in range(1, 4)])
        ):
            res[a] += 1
print(sum(res.values()), max([i for i in res if res[i] == max(res.values())]))