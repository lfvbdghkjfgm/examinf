# Solved by lfvbdghkjfgm
# https://lfvb.ru

text = open(r"C:\Users\aatop\Downloads\203_1.txt").readlines()
# text = open(r"1.txt").readlines()
n, k = map(int, text[0].split())
data = {}
for x in text[1:]:
    a, b = map(int, x.split())
    if a in data.keys():
        data[a].add(b)
    else:
        data[a] = {
            b,
        }
data1 = {}
for a, b in data.items():
    data1[a] = sorted(list(b))
mx = [0, 0]
for row, line in data1.items():
    lines = 0
    active_line = []
    for i in range(len(line)):
        if i == 0:
            active_line.append(line[i])
        elif line[i] - line[i - 1] == 1:
            active_line.append(line[i])
        else:
            if len(active_line) >= k:
                lines += 1
            active_line = [line[i]]
    if len(active_line) >= k:
        lines += 1
    if lines > mx[1] or lines == mx[1] and row > mx[0]:
        mx = [row, lines]
print(mx[::-1])