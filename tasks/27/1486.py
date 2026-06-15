# Solved by Владимир Д.
# Первая часть решения

from math import dist


with open("other/examinf/27/1486A.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    mean_x = sum(p[0] for p in clusters[i]) / len(clusters[i])
    mean_y = sum(p[1] for p in clusters[i]) / len(clusters[i])
    best_centroid[i] = [mean_x, mean_y]

print(best_centroid)
P_x = int((sum([x for x, y in best_centroid]) / len(clusters)) * 10_000)
P_y = int((sum([y for x, y in best_centroid]) / len(clusters)) * 10_000)
print(P_x, P_y)

# Вторая часть решения

from math import dist


with open("other/examinf/27/1486B.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)


best_centroid = [[] for _ in range(len(clusters))]
for i in range(len(clusters)):
    mean_x = sum(p[0] for p in clusters[i]) / len(clusters[i])
    mean_y = sum(p[1] for p in clusters[i]) / len(clusters[i])
    best_centroid[i] = [mean_x, mean_y]

print(best_centroid)
P_x = int((sum([x for x, y in best_centroid]) / len(clusters)) * 10_000)
P_y = int((sum([y for x, y in best_centroid]) / len(clusters)) * 10_000)
print(P_x, P_y)
