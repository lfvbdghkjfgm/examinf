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
m = 0
for p1 in clusters[0]:
    for p2 in clusters[0]:
        if dist(p1, p2) > m:
            m = dist(p1, p2)
            print(m, p1, p2)
print(m)
n = 0
for p1 in clusters[1]:
    for p2 in clusters[1]:
        if dist(p1, p2) > m:
            n = dist(p1, p2)
            print(n, p1, p2)
print(n)
P_x = 10000 * ((-1.355647 - 0.194696 + 3.035415 + 5.206956) / 4)
P_y = 10000 * ((3.106126 + 0.573149 + 9.006966 + 6.792227) / 4)
print(P_x, P_y)
print("16730", "48696")


# Б

k = 0
for p1 in clusters[2]:
    for p2 in clusters[2]:
        if dist(p1, p2) > k:
            k = dist(p1, p2)
            print(k, p1, p2)
print(k)

P_x = 10000 * ((1.219715 - 1.491394 + 6.785219 + 9.574408 - 2.22912 + 0.530401) / 6)
P_y = 10000 * ((10.761416 + 8.132521 + 6.553492 + 3.941747 - 1.631582 + 0.765846) / 6)
print(P_x, P_y)
print("23982", "47539")
