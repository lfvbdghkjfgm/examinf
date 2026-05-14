from math import dist

nums = [[float(i.replace(',','.')) for i in x.split()] for x in open('file.txt')]

# Сначала выводится количество кластеров, важно его проверить
# Если количество кластеров слишком маленькое, надо уменишить k
# Если слишком большое - увеличить k
k = 1

clusters = []
while nums:
    cluster = [nums.pop()]
    for star in cluster:
        s = [i for i in nums if dist(i,star) < k]
        for i in s:
            cluster.append(i)
            nums.remove(i)
    clusters.append(cluster)

print(len(clusters))

centres = []

for cluster in clusters:
    mn = [[],0]
    for star in cluster:
        s = sum([dist(star,i) for i in cluster])
        if s < mn[1]:
            mn = [star,s]
    centres.append(mn[0])

x = [i[0] for i in centres]
y = [i[1] for i in centres]
x = sum(x) / len(x)
y = sum(y) / len(y)

# В задаче может быть другой коэффициент, важно проверить!
print(x*10_000,y*10_000)
