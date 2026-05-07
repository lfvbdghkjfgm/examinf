data = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1024_4.txt")
]
data = data[1:]
tasks = {}

for a, b in data:
    if a not in tasks.keys():
        tasks[a] = set()
    tasks[a].add(b)

mx = [0, 0]

for a in sorted(tasks.keys()):
    d = sorted(list(tasks[a]))
    mx_line = 0
    cur_line = [d[0]]
    for i in d[1:]:
        if i - cur_line[-1] == 1:
            cur_line.append(i)
        else:
            mx_line = max(mx_line, len(cur_line))
            cur_line = [i]
    mx_line = max(mx_line, len(cur_line))
    if mx_line > mx[1]:
        mx = [a, mx_line]
print(*mx)
