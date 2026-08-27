# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import dist

data = [[float(i.replace(",", ".")) for i in x.split()] for x in open("1.txt")]

k = 0.5
clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [st for st in data if dist(star, st) < k]
        for st in sosed:
            data.remove(st)
            cluster.append(st)
    clusters.append(cluster)


clusters.sort(key=len)
clusters = clusters[1:]
print(len(clusters))
centres = []
for cluster in clusters:
    mn = [0, []]
    for star in cluster:
        s = sum([dist(i, star) for i in cluster])
        if s > mn[0]:
            mn = [s, star]
    centres.append(mn[1])

x = [i[0] for i in centres]
y = [i[1] for i in centres]
x = sum(x) / len(x)
y = sum(y) / len(y)
print(int(x * 10_000), int(y * 10_000))
