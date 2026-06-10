# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\26.txt")]

comps_ct = data[0][0]

computers = []

for i in range(1, comps_ct + 1):
    computers.append([i, -1, 0])

data = data[2:]
data.sort()

res = 0
for start, end in data:
    for comp in computers:
        if start > comp[1]:
            comp[1] = end
            t = end - start
            comp[2] += t * (t + 1) // 2
            res += 1
            break

print(res, max([i[2] for i in computers]))
