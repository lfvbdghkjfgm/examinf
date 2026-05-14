# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\736_1.txt")
]
data = data[1:]
data.sort()

res = [data[0]]

for start, end in data:
    if start >= res[-1][1] + 20:
        res.append([start, end])
    elif start >= res[-1][0] and end <= res[-1][1]:
        res[-1] = [start, end]

print(len(res), data[-1][0] - res[-2][1])