# Solved by lfvbdghkjfgm
# https://lfvb.ru


def to_15(num):
    res = []
    while num:
        res.append(num % 15)
        num //= 15
    return res[::-1]


t = to_15(3 * 15**1140 + 2 * 15**1025 + 15**923 - 3 * 15**85 + 2 * 15**74 + 3)
mx_line = 0
cur_line = [t[0]]
for i in t[1:]:
    if i == cur_line[-1]:
        cur_line.append(i)
        mx_line = max(mx_line, len(cur_line))
    else:
        cur_line = [i]
print(mx_line)
