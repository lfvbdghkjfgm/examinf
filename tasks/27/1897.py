# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import dist

# Файл А

k = 1

data = [x.replace(",", ".").split() for x in open(r"C:\Users\111\Downloads\27_A.txt")]
data = [[float(x), float(y), s] for x, y, s in data]

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

res = [10**6, []]
for star in clusters[0]:
    if (
        star[-1][0] == "M"
        and star[-1][-3:] == "III"
        and dist(star[:-1], centres[0][:-1]) < res[0]
    ):
        res = [
            dist(star[:-1], centres[0][:-1]),
            [int(abs(star[0]) * 10_000), int(abs(star[1]) * 10_000)],
        ]

print(*res[1])

# Файл Б

k = 1

data = [x.replace(",", ".").split() for x in open(r"C:\Users\111\Downloads\27_B.txt")]
data = [[float(x), float(y), s] for x, y, s in data]

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i[:-1], star[:-1]) < k]
        for st in sosed:
            data.remove(st)
            cluster.append(st)
    orange_gigants = 0
    for star in cluster:
        if star[-1][0] == "K" and star[-1][-3:] == "III":
            orange_gigants += 1
    clusters.append([cluster, orange_gigants])

print(len(clusters))

clusters.sort(key=lambda d: d[1])

centres = []
for cluster in clusters:
    mn = [10**6, []]
    for star in cluster[0]:
        s = sum([dist(i[:-1], star[:-1]) for i in cluster[0]])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

res = 0
for cluster in clusters:
    cluster = cluster[0]
    for star in cluster:
        if star[-1][0] == "G" and star[-1][-1] == "V" and len(star[-1]) == 3:
            s = max(
                [
                    dist(i[:-1], star[:-1])
                    for i in cluster
                    if i[-1][0] == "G" and i[-1][-1] == "V" and len(i[-1]) == 3
                ]
            )
            res = max(res, s)


print(int(dist(centres[0][:-1], centres[-1][:-1]) * 10_000), int(res * 10_000))
