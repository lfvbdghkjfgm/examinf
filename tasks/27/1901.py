# Solved by Владимир Д.
# Первая часть решения

from math import dist

with open("examinf/27/1901A.txt") as f:
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

dists = []
for i in range(len(clusters)):
    for point in clusters[i]:
        if "N" == point[-1][0] and "I" == point[-1][2:] and "9" == point[-1][1]:
            for centr in best_centroid:
                cur_dist = dist(centr[0:2], point[0:2])
                dists.append(cur_dist)

print(int(min(dists) * 10_000), int(max(dists) * 10_000))

# Вторая часть решения

from math import dist

with open("examinf/27/1901B.txt") as f:
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
    print(len(clusters[i]))
    min_sum_dist = float("inf")
    for p1 in clusters[i]:
        sum_dist = 0
        for p2 in clusters[i]:
            sum_dist += dist(p1[0:2], p2[0:2])

        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroid[i] = p1

ct1, ct2 = 0, 0
for point in clusters[0]:
    try:
        if int(point[-1][1]) > 7:
            ct1 += 1
    except:
        continue

for point in clusters[1]:
    try:
        if int(point[-1][1]) < 4:
            ct2 += 1
    except:
        continue

print(ct1, ct2)

# Solved by Анастасия


# import math
# l=[[d.replace(',','.') for d in x.split()] for x in open('1901.a.txt')]
# for p in range(len(l)):
#     l[p]=[float(l[p][0]),float(l[p][1]), l[p][2]]
# clusters=[[],[]]
# for p in l:
#     if p[1]>10:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centr=[[],[]]
# ind=0
# for x in clusters:
#     mn_rast=10**10
#     for y in x:
#         rast=0
#         for z in x:
#             rast+=math.dist(y[:-1],z[:-1])
#         if rast<mn_rast:
#             mn_rast=rast
#             centr[ind]=y
#     ind+=1
# print(centr)
# mn=[]
# for p in clusters[0]:
#     if p[-1][1]=='9' and p[-1][2:]=='I' and p[-1][0]=='N':
#         mn.append(math.dist(centr[0][:-1],p[:-1]))
#         mn.append(math.dist(centr[1][:-1], p[:-1]))
# for p in clusters[1]:
#     if p[-1][1]=='9' and p[-1][2:]=='I' and p[-1][0]=='N':
#         mn.append(math.dist(centr[1][:-1],p[:-1]))
#         mn.append(math.dist(centr[0][:-1], p[:-1]))
# print(int(min(mn)*10000), int(max(mn)*10000))
# print(mn)


import math
from pprint import pprint

l = [[d.replace(",", ".") for d in x.split()] for x in open("1901.b.txt")]
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[1] < 15:
        clusters[2].append(p)
    else:
        clusters[1].append(p)
centr = [[], [], []]
ind = 0
for x in clusters:
    print(len(x))
    mn_rast = 10**10
    for y in x:
        rast = 0
        for z in x:
            rast += math.dist(y[:-1], z[:-1])
        if rast < mn_rast:
            mn_rast = rast
            centr[ind] = y
    ind += 1
print(centr)
ct = 0
for p in clusters[2]:
    # print(p)
    if p[-1][1] == "8" or p[-1][1] == "9":
        ct += 1
k = 0
for p in clusters[1]:
    if p[-1][1] == "3" or p[-1][1] == "2" or p[-1][1] == "1":
        k += 1
print(ct, k)
