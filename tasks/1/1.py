# Solved by Влад

from math import *

f = open("test.txt")
points = []
epsilon = 1
clusters = []
for s in f:
    s = s.replace(",", ".")
    points.append(s.split())
while points:
    clusters.append([points[0]])
    del points[0]
    for c1 in clusters[-1]:
        for c2 in points[:]:
            t1 = [float(c1[0]), float(c1[1])]
            t2 = [float(c2[0]), float(c2[1])]
            if dist(t2, t1) < epsilon:
                clusters[-1].append(c2)
                points.remove(c2)
print(len(clusters))
best_centroids = [[] for i in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = 10**10
    for c1 in clusters[i]:
        sum_dist = 0
        for c2 in clusters[i]:
            t1 = [float(c1[0]), float(c1[1])]
            t2 = [float(c2[0]), float(c2[1])]
            sum_dist += dist(t1, t2)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroids[i] = c1
print(best_centroids)
print(len(clusters[0]), len(clusters[1]))

# A

A = []
OG = [
    clusters[0][i]
    for i in range(len(clusters[0]))
    if (
        "K" in clusters[0][i][2]
        and "III" in clusters[0][i][2]
        and "V" not in clusters[0][i][2]
    )
]
for i in range(len(OG)):
    A.append(
        [
            dist(
                [float(OG[i][0]), float(OG[i][1])],
                [float(best_centroids[0][0]), float(best_centroids[0][1])],
            ),
            OG[i],
        ]
    )
print(min(A))
print(4.781532 * 10000, 7.494832 * 10000)

# B

KG0 = [
    clusters[0][i]
    for i in range(len(clusters[0]))
    if (
        "M" in clusters[0][i][2]
        and "III" in clusters[0][i][2]
        and "V" not in clusters[0][i][2]
    )
]
KG1 = [
    clusters[1][i]
    for i in range(len(clusters[1]))
    if (
        "M" in clusters[1][i][2]
        and "III" in clusters[1][i][2]
        and "V" not in clusters[1][i][2]
    )
]
KG2 = [
    clusters[2][i]
    for i in range(len(clusters[2]))
    if (
        "M" in clusters[2][i][2]
        and "III" in clusters[2][i][2]
        and "V" not in clusters[2][i][2]
    )
]
print(len(KG0), len(KG1), len(KG2))
print(
    dist(
        [float(best_centroids[0][0]), float(best_centroids[0][1])],
        [float(best_centroids[2][0]), float(best_centroids[2][1])],
    )
    * 10000
)

ZS0 = [
    clusters[0][i]
    for i in range(len(clusters[0]))
    if (
        "G" in clusters[0][i][2]
        and "VI" in clusters[0][i][2]
        and "VII" not in clusters[0][i][2]
    )
]
ZS1 = [
    clusters[1][i]
    for i in range(len(clusters[1]))
    if (
        "G" in clusters[1][i][2]
        and "VI" in clusters[1][i][2]
        and "VII" not in clusters[1][i][2]
    )
]
ZS2 = [
    clusters[2][i]
    for i in range(len(clusters[2]))
    if (
        "G" in clusters[2][i][2]
        and "VI" in clusters[2][i][2]
        and "VII" not in clusters[2][i][2]
    )
]

res = []
for c1 in ZS0:
    for c2 in ZS0:
        t1 = [float(c1[0]), float(c1[1])]
        t2 = [float(c2[0]), float(c2[1])]
        if dist(t1, t2) != 0:
            res.append(dist(t1, t2))

for c1 in ZS1:
    for c2 in ZS1:
        t1 = [float(c1[0]), float(c1[1])]
        t2 = [float(c2[0]), float(c2[1])]
        if dist(t1, t2) != 0:
            res.append(dist(t1, t2))

for c1 in ZS2:
    for c2 in ZS2:
        t1 = [float(c1[0]), float(c1[1])]
        t2 = [float(c2[0]), float(c2[1])]
        if dist(t1, t2) != 0:
            res.append(dist(t1, t2))
print(min(res) * 10000)
