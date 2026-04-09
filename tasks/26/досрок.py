
data = [[int(i) for i in x.split()] for x in open('1.txt')]
tmp  = [i[1] for i in data]
sr = sum(tmp) / len(tmp)

dt = {}
for a,b,c in data:
    if a not in dt.keys():
        dt[a] = [b,0,0]
    if c == 0:
        dt[a][1] += 1
    else:
        dt[a][2] += 1

res = []
for a,b in dt.items():
    res.append([a]+b)
res = [i for i in res if i[1] > sr]
res.sort(key=lambda d: (-d[2],-d[1],d[3]))
print(res[0][1] * res[0][2],res[0][3])