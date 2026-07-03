# Solved by Влад


from math import *

f = open("test.txt")
points = [list(map(float, s.replace(",", ".").split())) for s in f]
epsilon = 1
clusters = []
while points:
    clusters.append([points[0]])
    del points[0]
    for c1 in clusters[-1]:
        for c2 in points[:]:
            if dist(c1, c2) < epsilon:
                clusters[-1].append(c2)
                points.remove(c2)
print(len(clusters))
best_centroids = [[] for i in range(len(clusters))]
for i in range(len(clusters)):
    min_sum_dist = 10**10
    for c1 in clusters[i]:
        sum_dist = 0
        for p1 in clusters[i]:
            sum_dist += dist(c1, p1)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            best_centroids[i] = c1
print(best_centroids)
print(len(clusters[0]), len(clusters[1]))
t = [1.0, 1.5]
print((dist(best_centroids[0], t) + dist(best_centroids[1], t)) * 10000)
print("344", "294354")

# B
k = 0
print(len(clusters[0]), len(clusters[1]), len(clusters[2]))
for i in range(len(clusters[1])):
    if (
        dist(clusters[1][i], best_centroids[1]) <= 1.2
        and dist(clusters[1][i], best_centroids[1]) != 0
    ):
        k += 1
print(k)
m = 1000
for i in range(len(clusters[0])):
    if dist(best_centroids[0], clusters[0][i]) != 0:
        m = min(m, dist(best_centroids[0], clusters[0][i]))
print(m * 10000)
print(152, 528)
