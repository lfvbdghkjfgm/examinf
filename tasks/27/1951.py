# Solved by Анастасия


# import math
# l=[[d for d in x.split()] for x in open('27.a.txt')]
# # print(len(l))
# for p in range(len(l)):
#     l[p]=[float(l[p][0]),float(l[p][1]),l[p][2]]
# clusters=[[],[]]
# for p in l:
#     if p[1]>15:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centr=[[],[]]
# ind=0
# for x in clusters:
#     # print(len(x))
#     mn_rast=10**10
#     for y in x:
#         rast=0
#         for z in x:
#             rast+=math.dist(y[:2],z[:2])
#         if rast<mn_rast:
#             mn_rast=rast
#             centr[ind]=y
#     ind+=1
# print(centr)
# mn=[]
# for d in clusters[1]:
#     if d[-1]=='VII':
#         mn.append([math.dist(d[:-1], centr[1][:-1]), d[:-1]])
# print(min(mn,key=lambda d: d[0]))
# print(int(4.830069*10000), int(7.06511*10000))


import math

l = [[d for d in x.split()] for x in open("27.b.txt")]
# print(len(l))
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[0] > 16:
        clusters[0].append(p)
    elif p[1] < 30:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centr = [[], [], []]
ind = 0
for x in clusters:
    # print(len(x))
    mn_rast = 10**10
    for y in x:
        rast = 0
        for z in x:
            rast += math.dist(y[:2], z[:2])
        if rast < mn_rast:
            mn_rast = rast
            centr[ind] = y
    ind += 1
print(centr)
k1 = 0
for d in clusters[0]:
    if d[-1][0] == "K" and d[-1][2:] == "III":
        k1 += 1
k2 = 0
for d in clusters[1]:
    if d[-1][0] == "K" and d[-1][2:] == "III":
        k2 += 1
k3 = 0
for d in clusters[2]:
    if d[-1][0] == "K" and d[-1][2:] == "III":
        k3 += 1
print(k1, k2, k3)
mn = math.dist(centr[0][:-1], centr[2][:-1])
b2 = []
for t in clusters[0]:
    for c in clusters[1]:
        if (
            t[-1][0] == "G"
            and t[-1][2:] == "V"
            and c[-1][0] == "G"
            and c[-1][2:] == "V"
        ):
            b2.append(math.dist(t[:-1], c[:-1]))
print(int(mn * 10000), int(max(b2) * 10000))

# Solved by Аня


import math

l = [[d for d in x.split()] for x in open("bite.9.27.a.txt")]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(",", ".")), float(l[x][1].replace(",", ".")), l[x][2]]
clusters = [[], []]
for p in l:
    if p[1] > 15:
        clusters[0].append(p)
    else:
        clusters[1].append(p)
centroids = [[], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10**10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
r = []
for x in clusters[1]:
    if x[-1] == "VII":
        r.append([math.dist(x[:-1], centroids[1][:-1]), x[:-1]])
print(min(r, key=lambda x: x[0]))
print(int(4.830069 * 10000), int(7.06511 * 10000))

import math

l = [[d for d in x.split()] for x in open("bite.9.27.b.txt")]
for x in range(len(l)):
    l[x] = [float(l[x][0].replace(",", ".")), float(l[x][1].replace(",", ".")), l[x][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 30 and p[0] > 16:
        clusters[0].append(p)
    elif p[1] > 30 and p[0] < 16:
        clusters[1].append(p)
    else:
        clusters[2].append(p)
centroids = [[], [], []]
ind = 0
for cluster in clusters:
    print(len(cluster))
    mn_sm_rast = 10**10
    for p1 in cluster:
        sm_rast = 0
        for p2 in cluster:
            sm_rast += math.dist(p1[:-1], p2[:-1])
        if sm_rast < mn_sm_rast:
            mn_sm_rast = sm_rast
            centroids[ind] = p1
    ind += 1
ct = 0
for x in clusters[0]:
    if x[-1][0] == "K" and x[-1][2:] == "III":
        ct += 1
# 0, 2\
mx = []
for x in clusters[0]:
    for y in clusters[2]:
        if (
            x[-1][0] == "G"
            and x[-1][2:] == "V"
            and y[-1][0] == "G"
            and y[-1][2:] == "V"
        ):
            mx.append(math.dist(x[:-1], y[:-1]))
print(int(max(mx) * 10_000))

print(int((math.dist(centroids[0][:-1], centroids[1][:-1])) * 10_000))
