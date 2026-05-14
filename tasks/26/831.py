# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\831_1.txt")]
data = data[1:]

new_data = []

for x in data:
    id = x[0]
    results = x[1:]
    sm = sum(results)
    sm_pol = sum([i for i in results if i > 0])
    ct = len([i for i in results if i != 0])
    new_data.append([id, sm, sm_pol, ct])

new_data.sort(key=lambda d: (-d[1], -d[2], -d[3], d[0]))

ct_pr = len(new_data) // 3
pr = new_data[:ct_pr]

for x in new_data:
    if x[1:] == pr[-1][1:] and x[0] not in [i[0] for i in pr]:
        pr.append(x)

last = 0
for x in new_data:
    if x not in pr:
        last = x[0]
        break

res = 0
for x in new_data:
    if x[1:] == new_data[1699][1:]:
        res += 1

print(last, res)