# Solved by Глеб Г.


import math

l = [[float(d.replace(",", ".")) for d in x.split()] for x in open("23a.txt")]
clusters = [[], []]
for point in l:
    if point[0] > 2:
        clusters[0].append(point)
    else:
        clusters[1].append(point)
centroids = [[], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid, point)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
a = [(centroids[0][0] + centroids[1][0]) / 2, ((centroids[0][1] + centroids[1][1]) / 2)]
print(
    int(math.dist(centroids[1], [2.1, 5.0]) * 10000),
    int(math.dist([2.1, 5.0], a) * 10000),
)


import math

l = [[float(d.replace(",", ".")) for d in x.split()] for x in open("23b.txt")]
clusters = [[], [], []]
for point in l:
    if point[0] > 3:
        clusters[0].append(point)
    elif point[1] < -2.5:
        clusters[1].append(point)
    else:
        clusters[2].append(point)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    mn_sm_rast = 10**10
    for centroid in cluster:
        sm_rast = 0
        for point in cluster:
            sm_rast += math.dist(centroid, point)
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = centroid
    ind += 1
ct1 = 0
ct2 = 0
for point in l:
    if math.dist(point, centroids[2]) <= 5:
        ct1 += 1
for point in l:
    if math.dist(point, centroids[1]) > 5:
        ct2 += 1
print(ct1, ct2)
