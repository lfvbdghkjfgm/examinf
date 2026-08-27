# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

k = 10
data = [list(map(int, i.split())) for i in open("1.txt")]
data.sort()

lines = [[0] * k]

for a, b in data:
    fl = False
    for i in range(len(lines)):
        for j in range(k):
            if lines[i][j] < a:
                lines[i][j] = b
                fl = True
                break
        if fl:
            break
    if not fl:
        lines.append([0] * k)
        lines[-1][0] = b
    ct = 0
    for line in lines:
        for home in line:
            if home > a:
                ct += 1

print(len(lines), ct)
