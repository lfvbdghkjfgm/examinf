
data = [[int(i) for i in x.split()] for x in open('1.txt')]
data.sort()
res = [[data[0][0],data[0][1]+15]]
for a,b in data:
    if a >= res[-1][0] and b+15 <= res[-1][1]:
        res[-1] = [a,b+15]
    elif a >= res[-1][1]:
        res.append([a,b+15])
print(len(res),data[-1][0] - res[-2][1] + 15)