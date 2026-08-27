# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\26.txt")]

data = sorted(data[1:])
data = [[start, start + ln] for start, ln in data]

res = [[0, 0]]

for start, end in data:
    if start > res[-1][1]:
        res.append([start, end])
    elif start >= res[-1][0] and end <= res[-1][1]:
        res[-1] = [start, end]
print(len(res) - 1, 10_000 - data[-1][1])
