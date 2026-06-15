# Solved by lfvbdghkjfgm
# https://lfvb.ru

from math import dist

data = [[float(i.replace(",", ".")) for i in x.split()] for x in open("1.txt")]

# для А k = 2 для Б k = 3
k = 3
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

# Solved by Анастасия


# l=[[float(d.replace(',','.')) for d in x.split()] for x in open('1304.a.txt')]
# clusters=[[],[]]
# for p in l:
#     if p[1]>0:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centoids=[[],[]]
# ind=0
# for cluster in clusters:
#     rast=10**10
#     for x in cluster:
#         mnrast=0
#         for y in cluster:
#             mnrast+=((x[0]-y[0])**2 + (x[1]-y[1])**2)**0.5
#         if mnrast<rast:
#             rast=mnrast
#             centoids[ind]=x
#     ind+=1
# # print(centoids)
# Px=int(((centoids[0][0]+centoids[1][0])/2)*10000)
# Py=int(((centoids[0][1]+centoids[1][1])/2)*10000)
# print(Px,Py)


l = [[float(d.replace(",", ".")) for d in x.split()] for x in open("1304.b.txt")]
clusters = [[], [], []]
for p in l:
    if p[0] < 1:
        clusters[0].append(p)
    elif p[1] > 10:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centoids = [[], [], []]
ind = 0
for cluster in clusters:
    rast = 10**10
    for x in cluster:
        mnrast = 0
        for y in cluster:
            mnrast += ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5
        if mnrast < rast:
            rast = mnrast
            centoids[ind] = x
    ind += 1
# print(centoids)
Px = int(((centoids[0][0] + centoids[1][0] + centoids[2][0]) / 3) * 10000)
Py = int(((centoids[0][1] + centoids[1][1] + centoids[2][1]) / 3) * 10000)
print(Px, Py)

# Solved by София


"""l=[[float(d.replace(',','.'))for d in x.split()]for x in open('1_a')]
clusters=[[],[]]
for point in l:
    if point[1]>10:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids=[[],[]]
ind=0
from math import *
for cluster in clusters:
    mn_sm_rast=10**10
    for centroid in cluster:
        sm_rast=0
        for point in cluster:
            sm_rast+=dist(centroid,point)
        if mn_sm_rast>sm_rast:
            mn_sm_rast=sm_rast
            centroids[ind]=centroid
    ind+=1
Px=int(((centroids[0][0]+centroids[1][0])/2)*10_000)
Py=int(((centroids[0][1]+centroids[1][1])/2)*10_000)
print(Px,Py)"""

l = [[float(d.replace(",", ".")) for d in x.split()] for x in open("1304_6.csv")]
clusters = [[], [], []]
for point in l:
    if point[0] < 5:
        clusters[0].append(point)
    elif point[1] > 10:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
from math import *

for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += dist(centroid, point)
        if mn_sm_rast > sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
Px = int(((centroids[0][0] + centroids[1][0] + centroids[2][0]) / 3) * 10_000)
Py = int(((centroids[0][1] + centroids[1][1] + centroids[2][1]) / 3) * 10_000)
print(Px, Py)
