from math import dist

data = [x.split() for x in open("1.txt")]
data = [
    [float(x[0].replace(",", ".")), float(x[1].replace(",", ".")), x[2]] for x in data
]
k = 1
red_gigant = [i for i in data if i[-1][0] == "Y" and i[-1][-3:] == "III"]

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(star[:2], i[:2]) < k]
        for i in sosed:
            data.remove(i)
            cluster.append(i)
    mn = [10**8, []]
    for star in cluster:
        s = sum([dist(star[:2], i[:2]) for i in cluster])
        if s < mn[0]:
            mn = [s, star]
    clusters.append([cluster, mn[1]])
print(len(clusters))
clusters.sort(key=lambda d: len(d[0]))
center_min = clusters[0][1]
mn = min([dist(center_min[:2], i[:2]) for i in red_gigant])
mx = max([dist(center_min[:2], i[:2]) for i in red_gigant])
print(abs(int(mn * 10_000)), abs(int(mx * 10_000)))
