# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [[int(i) for i in x.split()] for x in open(r"C:\Users\111\Downloads\1269_3.txt")]
k = nums[0][1]
nums = nums[1:]
data = []
for a, b, c, d, e in nums:
    data.append([b + c + d + e, e, a])
data.sort()
res = []


def get_data(score):
    return [i for i in data if i[0] == score]


for i in range(320, 0, -1):
    d = get_data(i)
    if len(d) < k:
        for i in d:
            res.append(i)
        k -= len(d)
    else:
        last_i = i
        break

print(sorted(res, key=lambda d: (d[0], d[1], -d[2]))[0][2], len(get_data(last_i)))
