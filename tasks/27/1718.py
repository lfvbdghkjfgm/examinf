# Solved by Иван П.


a = [[float(d) for d in x.split()] for x in open("1718b.txt")]
cls = [[], [], []]
for e in a:
    if 10 < e[1] < 20:
        cls[0].append(e)
    elif 20 < e[1] < 30:
        if e[0] < 18:
            cls[1].append(e)
        else:
            cls[2].append(e)
ds = [[[], []], [[], []], [[], []]]
ind = 0
for cl in cls:
    dmax = 0
    for p1 in cl:
        for p2 in cl:
            d = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
            if d > dmax:
                dmax = d
                ds[ind][0] = p1
                ds[ind][1] = p2
    ind += 1
# самый маленький третий
q1 = ((ds[2][0][0] - ds[2][1][0]) ** 2 + (ds[2][0][1] - ds[2][1][1]) ** 2) ** 0.5
dd = []
for cl in ds:
    for p in cl:
        dd.append(p)
q2 = 0
for p1 in dd:
    for p2 in dd:
        rast = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        if rast > q2:
            q2 = rast
print(int(q1 * 10000))
print(int(q2 * 10000))
