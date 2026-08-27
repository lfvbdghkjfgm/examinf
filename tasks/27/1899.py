# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import dist

# Файл А

data = [x.replace(",", ".").split() for x in open(r"C:\Users\111\Downloads\27_A.txt")]
data = [[float(x), float(y), s] for x, y, s in data]

k = 1
clusters = []
centres = []
while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i[:-1], star[:-1]) < k]
        for st in sosed:
            cluster.append(st)
            data.remove(st)
    clusters.append(cluster)
    mn = [10**10, []]
    for star in cluster:
        s = sum([dist(star[:-1], i[:-1]) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

mn = 10**10
mx = 0
centr = centres[0]
for star in clusters[1]:
    if star[-1][0] == "N" and star[-1][-2:] == "IV":
        mx = max(mx, dist(centr[:-1], star[:-1]))
        mn = min(mn, dist(centr[:-1], star[:-1]))
centr = centres[1]
for star in clusters[0]:
    if star[-1][0] == "N" and star[-1][-2:] == "IV":
        mx = max(mx, dist(centr[:-1], star[:-1]))
        mn = min(mn, dist(centr[:-1], star[:-1]))

print(int(mn * 10_000), int(mx * 10_000))

# Файл Б

data = [x.replace(",", ".").split() for x in open(r"C:\Users\111\Downloads\27_B.txt")]
data = [[float(x), float(y), s] for x, y, s in data]

k = 1
clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i[:-1], star[:-1]) < k]
        for st in sosed:
            cluster.append(st)
            data.remove(st)
    clusters.append(cluster)

clusters.sort(key=len)

centres = []
for cluster in clusters:
    mn = [10**10, []]
    for star in cluster:
        s = sum([dist(star[:-1], i[:-1]) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])
print(len(clusters))

b1 = max(
    [
        i[0]
        for i in clusters[-1]
        if i[-1][0] == "J" and i[-1][-1] == "V" and len(i[-1]) == 3
    ]
)
b2 = max(
    [
        i[1]
        for i in clusters[0]
        if i[-1][0] == "J" and i[-1][-1] == "V" and len(i[-1]) == 3
    ]
)

print(int(b1 * 10_000), int(b2 * 10_000))

# Solved by Владимир Д.
# Первая часть решения

from math import dist

with open("examinf/27/1899A.txt") as f:
    points = [
        [
            float(s.replace(",", ".").split()[0]),
            float(s.replace(",", ".").split()[1]),
            s.split()[2],
        ]
        for s in f
    ]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1[0:2], p2[0:2]) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1[0:2], p2[0:2])
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1


print(best_centroid)

mn_rast = []
for x in range(2):
    for p in clusters[x]:
        if p[2][0] == "N" and p[2][2:] == "IV":
            mn_rast.append(dist(best_centroid[0 if x == 1 else 1][:-1], p[:-1]))

print(int(min(mn_rast) * 10_000), int(max(mn_rast) * 10_000))

# Вторая часть решения

from math import dist

with open("examinf/27/1899B.txt") as f:
    points = [
        [
            float(s.replace(",", ".").split()[0]),
            float(s.replace(",", ".").split()[1]),
            s.split()[2],
        ]
        for s in f
    ]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1[0:2], p2[0:2]) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1[0:2], p2[0:2])
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1


mx = []
for p in clusters[0]:
    if p[2][0] == "J" and p[2][2:] == "V":
        mx.append(p[0])

mn = []
for p in clusters[2]:
    if p[2][0] == "J" and p[2][2:] == "V":
        mn.append(p[1])

print(int(max(mx) * 10_000), int(max(mn) * 10_000))
