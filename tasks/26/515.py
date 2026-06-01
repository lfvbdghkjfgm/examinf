# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open("1.txt")]
n = data[0][1]
data = data[1:]
data = [[a, b + c + d, e] for a, b, c, d, e in data]
data.sort(key=lambda d: (-d[1], -d[2], d[0]))


def get_data(score):
    return [i for i in data if i[1] == score]


last_score = 0
half_score = 0

for i in range(300, 0, -1):
    t = get_data(i)
    if not t:
        continue
    if len(t) < n:
        n -= len(t)
        last_score = i
    else:
        half_score = i
        break

print(get_data(last_score)[-1][0], len(get_data(half_score)))
