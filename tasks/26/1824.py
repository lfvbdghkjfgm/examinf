# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open("1824_1.txt")]
data = data[1:]
data.sort()

empl_ct = 0
cur_timer = 0
mx_time = 0
changes = []

for i in range(0, 1440 + 1):
    ct = 0
    for x in data:
        if x[0] <= i < x[1]:
            ct += 1
    if ct == empl_ct:
        cur_timer += 1
    else:
        changes.append(i)
        mx_time = max(mx_time, cur_timer)
        cur_timer = 1
    empl_ct = ct
print(changes[-2], mx_time)
