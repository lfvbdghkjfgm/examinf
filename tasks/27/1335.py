# Solved by lfvbdghkfjgm
# https://lfvb.ru

from math import dist

data = [[float(i.replace(",", ".")) for i in x.split()] for x in open("1.txt")]
# для А k = 3 для Б k = 7
k = 7
clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [st for st in data if dist(star, st) < k]
        for st in sosed:
            data.remove(st)
            cluster.append(st)
    clusters.append(cluster)

print(len(clusters))

centres = []
for cluster in clusters:
    mn = [10**8, []]
    for star in cluster:
        s = sum([dist(i, star) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    centres.append(mn[1])

x = [i[0] for i in centres]
y = [i[1] for i in centres]
x = sum(x) / len(x)
y = sum(y) / len(y)
print(abs(int(x * 10_000)), abs(int(y * 10_000)))

# Solved by Данзан С.

import math

l = [[float(d.replace(",", ".")) for d in x.split()] for x in open("17_b.txt")]
clusters = [[], [], []]
for p in l:
    if p[0] < 65:
        clusters[0].append(p)
    elif p[0] > 100:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for p in cluster:
            sm_rast += math.dist(centroid, p)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
Px = int((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3 * 10000)
Py = int((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3 * 10000)
print(Px, Py)

# Solved by Анастасия

# l=[[float(d.replace(',','.')) for d in x.split()] for x in open('1335.a.txt')]
# cl=[[],[]]
# for p in l:
#     if p[0]>20:
#         cl[0].append(p)
#     else:
#         cl[1].append(p)
# centr=[[],[]]
# ind=0
# for x in cl:
#     sr=10**10
#     for y in x:
#         rast=0
#         for z in x:
#             rast+=((y[0]-z[0])**2 + (y[1]-z[1])**2)**0.5
#         if rast<sr:
#             sr=rast
#             centr[ind]=y
#     ind+=1
# # print(centr)
# Px=int((centr[0][0]+centr[1][0])/2*10000)
# Py=int((centr[0][1]+centr[1][1])/2*10000)
# print(Px,Py)


l = [[float(d.replace(",", ".")) for d in x.split()] for x in open("1335.b.txt")]
cl = [[], [], []]
for p in l:
    if p[0] > 100:
        cl[0].append(p)
    elif p[0] < 64:
        cl[1].append(p)
    else:
        cl[2].append(p)
centr = [[], [], []]
ind = 0
for x in cl:
    sr = 10**10
    for y in x:
        rast = 0
        for z in x:
            rast += ((y[0] - z[0]) ** 2 + (y[1] - z[1]) ** 2) ** 0.5
        if rast < sr:
            sr = rast
            centr[ind] = y
    ind += 1
# print(centr)
Px = int((centr[0][0] + centr[1][0] + centr[2][0]) / 3 * 10000)
Py = int((centr[0][1] + centr[1][1] + centr[2][1]) / 3 * 10000)
print(Px, Py)
