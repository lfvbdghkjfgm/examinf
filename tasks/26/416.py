# структура хранения:

# bancomats  = [
# 	[
# 	  номер банкомата,
# 	    [
# 		[старт обслуживания первого клиента, конец обслуживания первого клиента],
# 		...
# 		[старт обслуживания последнего клиента, конец обслуживания последнего клиента]
# 	    ]
# 	],
# 	...
# ]


data = [[int(i) for i in x.split()] for x in open("1.txt")]
n = data[0][0]
data = [[i] + d for i, d in enumerate(data[1:], 1)]
data.sort(key=lambda d: (d[1], d[0]))
data = [i[1:] for i in data]

bancomats = []

for i in range(1, n + 1):
    bancomats.append([i, [[0, 0]]])

max_wait = 0
for start, time in data:
    bancomats.sort(key=lambda d: (d[1][-1][1], d[0]))
    if start >= bancomats[0][1][-1][1]:
        bancomats[0][1].append([start, start + time])
    else:
        wait = bancomats[0][1][-1][1] - start
        max_wait = max(max_wait, wait)
        bancomats[0][1].append([bancomats[0][1][-1][1], bancomats[0][1][-1][1] + time])

print(max_wait, max(bancomats, key=lambda d: (len(d[1]), -d[0]))[1][-1][0])
