# Solved by Вадим С.


from math import *

l = [
    [[float(d.replace(",", ".")) for d in x.split()[:-1]], x.split()[-1]]
    for x in open("1810_4.txt")
]
clusters = [[], []]
for p in l:
    if p[0][1] > 8:
        clusters[0].append(p)
    #    elif p[0][0] > 20:
    #       clusters[2].append(p)
    else:
        clusters[1].append(p)
clusters = sorted(clusters, key=len)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mx_sm_rast = 10**10
    for centroid in cluster:
        mx_rast = 0
        for p in cluster:
            mx_rast += dist(centroid[0], p[0])
        if mx_rast < mx_sm_rast:
            mx_sm_rast = mx_rast
            centroids[ind] = centroid
    ind += 1
sz = [x for x in l if x[1][:2] == "L3"]
rast = [[], []]
ind = 0
for p in centroids:
    for s in sz:
        if s != p:
            rast[ind].append(dist(p[0], s[0]))
    ind += 1
print(int(max(rast[0]) * 10000), int(max(rast[1]) * 10000))

from math import *

l = [
    [[float(d.replace(",", ".")) for d in x.split()[:-1]], x.split()[-1][0]]
    for x in open("1810_5.txt")
]
clusters = [[], [], []]
for p in l:
    if p[0][1] > 23:
        clusters[0].append(p)
    elif p[0][0] > 20:
        clusters[2].append(p)
    else:
        clusters[1].append(p)
clusters = sorted(clusters, key=lambda d: d.count("L"))
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mx_sm_rast = 10**10
    for centroid in cluster:
        mx_rast = 0
        for p in cluster:
            mx_rast += dist(centroid[0], p[0])
        if mx_rast < mx_sm_rast:
            mx_sm_rast = mx_rast
            centroids[ind] = centroid
    ind += 1
sz = [x for x in l if x[1] == "L"]
rast = []
for s in sz:
    for z in sz:
        rast.append(dist(s[0], z[0]))
print(int(dist(centroids[0][0], centroids[2][0]) * 10000), int(max(rast) * 10000))
