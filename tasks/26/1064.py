# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\1064_3.txt")]

data = {}

for a, b in nums:
    if a not in data.keys():
        data[a] = [b]
    else:
        data[a].append(b)


mx = [0, 0]

for a, b in data.items():
    b = sorted(set(b))
    mx_line = 0
    len_line = 1
    for i in range(1, len(b)):
        if b[i] - b[i - 1] == 1:
            len_line += 1
        else:
            mx_line = max(mx_line, len_line)
            len_line = 1
    mx_line = max(mx_line, len_line)
    if mx_line > mx[1] or mx_line == mx[1] and a < mx[0]:
        mx = [a, mx_line]

print(*mx)
