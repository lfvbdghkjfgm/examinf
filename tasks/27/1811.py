# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

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

# Solved by Владимир Д.
# Первая часть решения

from math import dist

with open("other/examinf/27/1811A.txt") as f:
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


yl_ct = []
for i in range(len(clusters)):
    ct = 0
    for point in clusters[i]:
        if "Z" in point[-1]:
            ct += 1

    yl_ct.append(ct)

print(min(yl_ct), max(yl_ct))

# Вторая часть решения

from math import dist

with open("other/examinf/27/1811B.txt") as f:
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


dists = []
for i in range(len(clusters)):
    for point in clusters[i]:
        if "L" in point[-1] and "V" == point[-1][-1]:
            cur_dist = dist(best_centroid[i][0:2], point[0:2])
            dists.append(cur_dist)

print(int(min(dists) * 10_000), int(max(dists) * 10_000))

# Solved by Анастасия


import math

# l=[[d.replace(',','.') for d in x.split()] for x in open('1811.a.txt')]
# # print(len(l))
# for p in range(len(l)):
#     l[p]=[float(l[p][0]),float(l[p][1]),l[p][2]]
# clusters=[[],[]]
# for p in l:
#     if p[1]>10:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centr=[[],[]]
# ind=0
# for x in clusters:
#     # print(len(x))
#     mn_rast=10**10
#     for y in x:
#         rast=0
#         for z in x:
#             rast+=math.dist(y[:2],z[:2])
#         if rast<mn_rast:
#             mn_rast=rast
#             centr[ind]=y
#     ind+=1
# # print(centr)
# mn1=0
# for d in clusters[0]:
#     if d[-1][0]=='Z':
#         mn1+=1
#         # print(d)
# mn2=0
# for d in clusters[1]:
#     if d[-1][0]=='Z':
#         mn2+=1
# print(min(mn1,mn2), max(mn1,mn2))


import math

l = [[d.replace(",", ".") for d in x.split()] for x in open("1811.b.txt")]
# print(len(l))
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[1] < 15:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centr = [[], [], []]
ind = 0
for x in clusters:
    # print(len(x))
    mn_rast = 10**10
    for y in x:
        rast = 0
        for z in x:
            rast += math.dist(y[:2], z[:2])
        if rast < mn_rast:
            mn_rast = rast
            centr[ind] = y
    ind += 1
# print(centr)
mn = []
for d in clusters[1]:
    if d[-1][0] == "L" and d[-1][2:] == "V":
        # print(d[-1])
        mn.append(math.dist(centr[1][0:-1], d[:-1]))
for d in clusters[2]:
    if d[-1][0] == "L" and d[-1][2:] == "V":
        # print(d[-1])
        mn.append(math.dist(centr[2][0:-1], d[:-1]))
print((int(min(mn) * 10000)), int(max(mn) * 10000))

# Solved by Глеб Г.


import math

l = [[d for d in x.split()] for x in open("24a.txt")]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(",", ".")), float(l[x][1].replace(",", ".")), l[x][2]]
clusters = [[], []]
for point in l:
    if point[1] > 10:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
ct1 = 0
ct2 = 0
for point in clusters[0]:
    if point[2][0] == "Z":
        ct1 += 1
for point in clusters[1]:
    if point[2][0] == "Z":
        ct2 += 1
print(ct1, ct2)


import math

l = [[d for d in x.split()] for x in open("24b.txt")]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(",", ".")), float(l[x][1].replace(",", ".")), l[x][2]]
clusters = [[], [], []]
for point in l:
    if point[0] > 20:
        clusters[0].append(point)
    elif point[1] > 22:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        mn_rast = 0
        for point in cluster:
            mn_rast += math.dist(centroid[:-1], point[:-1])
        if mn_rast < mn_sm_rast:
            mn_sm_rast = mn_rast
            centroids[ind] = centroid
    ind += 1
print(centroids)
mn_rast = []
for p1 in clusters[0]:
    if p1[2][0] == "L" and p1[2][-1] == "V" and p1 != centroids[0]:
        mn_rast.append(int(math.dist(centroids[0][:-1], p1[:-1]) * 10000))
for p1 in clusters[1]:
    if p1[2][0] == "L" and p1[2][-1] == "V" and p1 != centroids[1]:
        mn_rast.append(int(math.dist(centroids[1][:-1], p1[:-1]) * 10000))
for p1 in clusters[2]:
    if p1[2][0] == "L" and p1[2][-1] == "V" and p1 != centroids[2]:
        mn_rast.append(int(math.dist(centroids[2][:-1], p1[:-1]) * 10000))
print(min(mn_rast), max(mn_rast))
