# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

text = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\514_3.txt")]
data = {}
tmp = [i[1] for i in text]
sr = sum(tmp) / len(tmp)
for id, price, act in text:
    if price < sr:
        continue
    if id not in data.keys():
        data[id] = [id, price, 0, 0]
    if act == 0:
        data[id][2] += 1
    else:
        data[id][3] += 1
data = list(data.values())
data = sorted(data, key=lambda d: (-d[2], -d[1], d[3]))
print(data[0][2] * data[0][1], data[0][3])
