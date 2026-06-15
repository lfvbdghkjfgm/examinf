# Solved by lfvbdghkjfgm
# https://lfvb.ru

from math import dist

# Файл А

k = 1

data = [
    [float(i.replace(",", ".")) for i in x.split()]
    for x in open(r"C:\Users\111\Downloads\27_A.txt")
]

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i, star) < k]
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
        s = sum([dist(i, star) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

res = 0
for star in clusters[0]:
    if star[0] <= centres[0][0]:
        res += 1

print(res, int(dist(centres[0], centres[1]) * 10_000))

# Файл Б

k = 1

data = [
    [float(i.replace(",", ".")) for i in x.split()]
    for x in open(r"C:\Users\111\Downloads\27_B.txt")
]

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(i, star) < k]
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
        s = sum([dist(i, star) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

res = 0
for star in clusters[1]:
    if abs(star[0] - centres[1][0]) <= 1 and abs(star[1] - centres[1][1]) <= 1:
        res += 1
print(res, int(abs(centres[0][1] - centres[2][1]) * 10_000))

# Solved by Владимир Д.
# Первая часть решения

from math import dist

with open("other/examinf/27/1896A.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1


print(best_centroid)
print(len(clusters[0]), len(clusters[1]))

print(len([d for d in clusters[0] if d[0] <= best_centroid[0][0]]))
print(int(dist(best_centroid[0], best_centroid[1]) * 10_000))

# Вторая часть решения

from math import dist

with open("other/examinf/27/1896B.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1, p2)

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1


print(best_centroid)
print(len(clusters[0]), len(clusters[1]), len(clusters[2]))


ct = 0
for p in clusters[1]:
    if best_centroid[1][0] - 1 <= p[0] <= best_centroid[1][0] + 1:
        if best_centroid[1][1] - 1 <= p[1] <= best_centroid[1][1] + 1:
            ct += 1

print(ct)
print(int((best_centroid[0][1] - best_centroid[2][1]) * 10_000))
