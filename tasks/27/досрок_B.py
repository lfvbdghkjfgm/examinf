from math import dist

data = [x.split() for x in open('1.txt')]
data = [[float(x[0].replace(',','.')),float(x[1].replace(',','.')),x[2]] for x in data]
k = 1

clusters = []

while data:
    cluster = [data.pop()]
    for star in cluster:
        sosed = [i for i in data if dist(star[:2],i[:2]) < k]
        for i in sosed:
            data.remove(i)
            cluster.append(i)
    mn = [10**8,[]]
    for star in cluster:
        s = sum([dist(star[:2],i[:2]) for i in cluster])
        if s < mn[0]:
            mn = [s,star]
    yellow_gigants = [i for i in cluster if i[-1][0] == 'Z' and i[-1][-2:]=='IV']
    clusters.append([cluster,mn[1],len(yellow_gigants)])

print(len(clusters))



mn = 10**8
mx = 0
for cluster in clusters:
    cluster = cluster[0]
    yellow_gigants = [i for i in cluster if i[-1][0] == 'Z' and i[-1][-2:]=='IV']
    for i in range(len(yellow_gigants)):
        for j in range(i+1,len(yellow_gigants)):
            d = dist(yellow_gigants[i][:2],yellow_gigants[j][:2])
            mn = min(d,mn)


clusters.sort(key=lambda d:d[-1])
d = dist(clusters[0][1][:2],clusters[-1][1][:2])

print(abs(int(mn*10_000)),abs(int(d*10_000)))