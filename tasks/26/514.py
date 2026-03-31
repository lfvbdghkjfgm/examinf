
nums = [[int(i) for i in x.split()] for x in open('1.txt')]

sold = {}
ost = {}
price = {}
tmp  = [i[1] for i in nums]
sr = sum(tmp) / len(tmp)

for a,b,c in nums:
    if a not in price.keys():
        price[a] = b

for i in price.keys():
    sold[i] = 0
    ost[i] = 0

for a,b,c in nums:
    if b > sr:
        if c == 0:
            sold[a] += 1
        if c == 1:
            ost[a] += 1

print([i for i in sold if sold[i] == max(sold.values())])
print(sold[51786])
print(sold[46481])
print(price[51786])
print(price[46481])
print(ost[51786])
print(ost[46481])

print(sold[46481]*price[46481],ost[46481])