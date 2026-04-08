data = [[int(i) for i in x.split()] for x in open('1.txt')]
data.sort()
data = [[a,a+b] for a,b in data]
res = [data[0]]

for a,b in data:
    if a >= res[-1][0] and b <= res[-1][1]:
        res[-1] = [a,b]
    elif a >= res[-1][1]:
        res.append([a,b])

res[-1] = data[-1]
    
print(res)
print(len(res),res[-1][0] - res[-2][1])