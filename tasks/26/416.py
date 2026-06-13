# Solved by lfvbdghkjfgm
# https://lfvb.ru

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


data = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\416_1.txt")
]
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

# Второй вариант решения (Более простой и одновремменно более сложный)

data = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\416_1.txt")
]

n = data[0][0]
data = sorted(data[1:], key=lambda d: d[0])

bancomats = {}
for i in range(1, n + 1):
    bancomats[i] = {"count": 0, "last_start": -1, "last_end": -1}


def find_bancomat(time):
    cur_banc = 1
    is_free = 0
    for number, info in bancomats.items():
        if info["last_end"] <= time and is_free == 0:
            cur_banc = number
            is_free = 1
            break
        elif (
            info["last_end"] > time
            and info["last_end"] < bancomats[cur_banc]["last_end"]
            and is_free == 0
        ):
            cur_banc = number
    return cur_banc


max_wait = 0
for start, time in data:
    num = find_bancomat(start)
    bancomats[num]["count"] += 1
    if bancomats[num]["last_end"] <= start:
        bancomats[num]["last_start"] = start
        bancomats[num]["last_end"] = start + time
    else:
        wait = bancomats[num]["last_end"] - start
        max_wait = max(max_wait, wait)
        bancomats[num]["last_start"] = bancomats[num]["last_end"]
        bancomats[num]["last_end"] = bancomats[num]["last_end"] + time

max_users = 0
max_users_bancomat_number = 0

for number, info in bancomats.items():
    if info["count"] > max_users:
        max_users = info["count"]
        max_users_bancomat_number = number

print(max_wait, bancomats[max_users_bancomat_number]["last_start"])
