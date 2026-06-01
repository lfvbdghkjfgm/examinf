# Solved by lfvbdghkfjgm
# https://lfvb.ru

from math import dist

k = 1
data = [
    x.replace(",", ".").split() for x in open(r"C:\Users\aatop\Downloads\1811_5.txt")
]
data = [[float(x), float(y), stat] for x, y, stat in data]

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i[:-1], star[:-1]) < k]
        for i in sosed:
            cluster.append(i)
            data.remove(i)
    clusters.append(cluster)

print(len(clusters))

# файл А
yellow_ct = []
for cluster in clusters:
    ct = 0
    for star in cluster:
        if star[2][0] == "Z":
            ct += 1
    yellow_ct.append(ct)
print(min(yellow_ct), max(yellow_ct))

# файл Б
blue_dist = []

for cluster in clusters:
    mn = [10**8, []]
    for star in cluster:
        s = sum([dist(i[:-1], star[:-1]) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centre = mn[1]
    mn_dist = 10**10
    mx_dist = 0

    for star in cluster:
        if star[2][0] == "L" and star[2][-1] == "V":
            d = dist(centre[:-1], star[:-1])
            if d < mn_dist:
                mn_dist = d
            if d > mx_dist:
                mx_dist = d
    blue_dist.append(mn_dist)
    blue_dist.append(mx_dist)

print(int(min(blue_dist) * 10_000), int(max(blue_dist) * 10_000))
