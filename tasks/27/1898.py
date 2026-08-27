# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import dist

# Файл А

k = 1

data = [x.replace(",", ".").split() for x in open(r"C:\Users\111\Downloads\27_A.txt")]
data = [[float(x), float(y), s] for x, y, s in data]
stars = data.copy()

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i[:-1], star[:-1]) < k]
        for st in sosed:
            data.remove(st)
            cluster.append(st)
    clusters.append(cluster)

print(len(clusters))

clusters.sort(key=len)

centres = []
for cluster in clusters:
    mn = [10**6, []]
    for star in cluster:
        s = sum([dist(i[:-1], star[:-1]) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

a1 = max(
    [
        dist(centres[0][:-1], i[:-1])
        for i in stars
        if i[-1][0] == "L" and i[-1][1] == "3"
    ]
)
a2 = max(
    [
        dist(centres[1][:-1], i[:-1])
        for i in stars
        if i[-1][0] == "L" and i[-1][1] == "3"
    ]
)
print(int(a1 * 10_000), int(a2 * 10_000))


# Файл Б

k = 1

data = [x.replace(",", ".").split() for x in open(r"C:\Users\111\Downloads\27_B.txt")]
data = [[float(x), float(y), s] for x, y, s in data]
stars = data.copy()

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i[:-1], star[:-1]) < k]
        for st in sosed:
            data.remove(st)
            cluster.append(st)
    blue_stars = 0
    for star in cluster:
        if star[-1][0] == "L":
            blue_stars += 1
    clusters.append([cluster, blue_stars])

print(len(clusters))

clusters.sort(key=lambda d: d[1])

centres = []
for cluster in clusters:
    cluster = cluster[0]
    mn = [10**6, []]
    for star in cluster:
        s = sum([dist(i[:-1], star[:-1]) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

blue_stars = [i for i in stars if i[-1][0] == "L"]
mx = 0
for cl in clusters:
    cl = cl[0]
    for star in cl:
        if star[-1][0] == "L":
            s = max([dist(star[:-1], i[:-1]) for i in blue_stars if i not in cl])
            mx = max(mx, s)

print(int(dist(centres[0][:-1], centres[-1][:-1]) * 10_000), int(mx * 10_000))
