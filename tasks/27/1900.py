# Solved by Анастасия


# import math
# l=[[d.replace(',','.') for d in x.split()] for x in open('1900.a.txt')]
# for p in range(len(l)):
#     l[p]=[float(l[p][0]),float(l[p][1]),l[p][2]]
# clusters=[[],[]]
# for p in l:
#     if p[1]>10:
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# centr=[[],[]]
# ind=0
# for x in clusters:
#     mn_rast=10**10
#     for y in x:
#         rast=0
#         for z in x:
#             rast+=math.dist(y[:-1],z[:-1])
#         if rast<mn_rast:
#             mn_rast=rast
#             centr[ind]=y
#     ind+=1
# print(centr)
# k1=0
# for p in clusters[0]:
#     if p[-1][1]=='5' and p[-1][0]=='G':
#         k1+=1
# k2=0
# for p in clusters[1]:
#     if p[-1][1]=='5' and p[-1][0]=='G':
#         k2+=1
# print(k1,k2)
# print(int(centr[1][0]*10000), int(centr[0][1]*10000))


import math

l = [[d.replace(",", ".") for d in x.split()] for x in open("1900.b.txt")]
for p in range(len(l)):
    l[p] = [float(l[p][0]), float(l[p][1]), l[p][2]]
clusters = [[], [], []]
for p in l:
    if p[1] > 22:
        clusters[0].append(p)
    elif p[1] < 15:
        clusters[2].append(p)
    else:
        clusters[1].append(p)
centr = [[], [], []]
ind = 0
for x in clusters:
    print(len(x))
    mn_rast = 10**10
    for y in x:
        rast = 0
        for z in x:
            rast += math.dist(y[:-1], z[:-1])
        if rast < mn_rast:
            mn_rast = rast
            centr[ind] = y
    ind += 1
print(centr)
mx = []
mn = []
for p in clusters[2]:
    if p[-1][2:] == "II":
        mx.append(math.dist(p[:-1], centr[2][:-1]))
for p in clusters[0]:
    if p[-1][2:] == "II":
        mn.append(math.dist(p[:-1], centr[0][:-1]))
print(int(sum(mx) / len(mx) * 10000), int(sum(mn) / len(mn) * 10000))
