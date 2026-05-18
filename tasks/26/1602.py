# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [[int(i) for i in x.split()] for x in open("1.txt")]

data = {}
for task, home, enter in nums:
    if home not in data.keys():
        data[home] = {}
    if enter not in data[home].keys():
        data[home][enter] = []
    data[home][enter].append(task)

res = [0, 0, []]

for home, enters in data.items():
    mx_line = []
    ents = sorted(enters.keys())
    cur_line = [ents[0]]
    for i in ents[1:]:
        if i - cur_line[-1] == 1:
            cur_line.append(i)
        else:
            if (
                len(cur_line) > len(mx_line)
                or len(cur_line) == len(mx_line)
                and max(enters[cur_line[0]]) > max(enters[mx_line[0]])
            ):
                mx_line = cur_line.copy()
            cur_line = [i]
    if cur_line:
        if (
            len(cur_line) > len(mx_line)
            or len(cur_line) == len(mx_line)
            and max(enters[cur_line[0]]) > max(enters[mx_line[0]])
        ):
            mx_line = cur_line.copy()
    if (
        len(mx_line) > len(res[-1])
        or len(mx_line) == len(res[-1])
        and max(enters[mx_line[0]]) > res[1]
    ):
        res = [home, max(enters[mx_line[0]]), mx_line]

print(res[0], res[-1][0])