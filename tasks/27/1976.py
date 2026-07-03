# Solved by Аня


import math

l = [[d for d in x.split()] for x in open("27a.txt")]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(",", ".")), float(l[x][1].replace(",", ".")), l[x][2]]
clusters = [[], []]
for p in l:
    if p[1] > 15:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10**10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
mn = []
for x in clusters[1]:
    if x[-1][2:] == "IV" or x[-1][2:] == "V":
        mn.append([math.dist(x[:-1], centroids[1][:-1]), x])
print(min(mn, key=lambda d: d[0]))
print(int(4.889805 * 10_000), int(7.298746 * 10_000))

import math

l = [[d for d in x.split()] for x in open("27b.txt")]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(",", ".")), float(l[x][1].replace(",", ".")), l[x][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 30 and p[0] > 16:
        clusters[0].append(p)
    elif p[1] > 30 and p[0] < 16:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10**10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
ct = 0
for x in clusters[2]:
    if x[-1][0] == "K" or x[-1][0] == "M":
        ct += 1
mx = []
for x in clusters[0]:
    for y in clusters[0]:
        if (x[-1][0] == "G" or x[-1][0] == "F") and (
            y[-1][0] == "G" or y[-1][0] == "F"
        ):
            if math.dist(x[:-1], y[:-1]) != 0:
                mx.append(math.dist(x[:-1], y[:-1]))
for x in clusters[1]:
    for y in clusters[1]:
        if (x[-1][0] == "G" or x[-1][0] == "F") and (
            y[-1][0] == "G" or y[-1][0] == "F"
        ):
            if math.dist(x[:-1], y[:-1]) != 0:
                mx.append(math.dist(x[:-1], y[:-1]))
for x in clusters[2]:
    for y in clusters[2]:
        if (x[-1][0] == "G" or x[-1][0] == "F") and (
            y[-1][0] == "G" or y[-1][0] == "F"
        ):
            if math.dist(x[:-1], y[:-1]) != 0:
                mx.append(math.dist(x[:-1], y[:-1]))

print(
    int((math.dist(centroids[0][:-1], centroids[2][:-1])) * 10_000),
    int(max(mx) * 10_000),
)

# Solved by Анастасия


# import math
# l=[[d.replace(',','.') for d in x.split()] for x in open('27.a.txt')]
# for p in range(len(l)):
#     l[p]=[float(l[p][0]),float(l[p][1]),l[p][2]]
# clusters=[[],[]]
# for p in l:
#     if p[1]>15:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centr=[[],[]]
# ind=0
# for x in clusters:
#     mn_rast=10**10
#     print(len(x))
#     for y in x:
#         rast=0
#         for z in x:
#             rast+=math.dist(y[:2],z[:2])
#         if rast<mn_rast:
#             mn_rast=rast
#             centr[ind]=y
#     ind+=1
# print(centr)
# d=[]
# for p in clusters[1]:
#     if p[-1][2:]=='IV' or p[-1][2:]=='V':
#         d.append([(math.dist(p[:-1],centr[1][:-1])),p])
# print(min(d,key=lambda d:d[0]))
# print(int(4.889805*10000), int(7.298746*10000))


import math

l = [[d.replace(",", ".") for d in x.split()] for x in open("27.b.txt")]
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[0] > 16:
        clusters[0].append(p)
    elif p[1] < 30:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centr = [[], [], []]
ind = 0
for x in clusters:
    mn_rast = 10**10
    print(len(x))
    for y in x:
        rast = 0
        for z in x:
            rast += math.dist(y[:2], z[:2])
        if rast < mn_rast:
            mn_rast = rast
            centr[ind] = y
    ind += 1
print(centr)
k1 = 0
for p in clusters[0]:
    if p[-1][0] == "K" or p[-1][0] == "M":
        k1 += 1
k2 = 0
for p in clusters[1]:
    if p[-1][0] == "K" or p[-1][0] == "M":
        k2 += 1
k3 = 0
for p in clusters[2]:
    if p[-1][0] == "K" or p[-1][0] == "M":
        k3 += 1
print(k1, k2, k3)
d = math.dist(centr[0][:-1], centr[1][:-1])
c = []
for p in clusters[0]:
    for t in clusters[0]:
        if (
            p != t
            and (p[-1][0] == "G" or p[-1][0] == "F")
            and (t[-1][0] == "G" or t[-1][0] == "F")
        ):
            c.append(math.dist(p[:-1], t[:-1]))
for p in clusters[1]:
    for t in clusters[1]:
        if (
            p != t
            and (p[-1][0] == "G" or p[-1][0] == "F")
            and (t[-1][0] == "G" or t[-1][0] == "F")
        ):
            c.append(math.dist(p[:-1], t[:-1]))

for p in clusters[2]:
    for t in clusters[2]:
        if (
            p != t
            and (p[-1][0] == "G" or p[-1][0] == "F")
            and (t[-1][0] == "G" or t[-1][0] == "F")
        ):
            c.append(math.dist(p[:-1], t[:-1]))

print(int(d * 10000), int(max(c) * 10000))
