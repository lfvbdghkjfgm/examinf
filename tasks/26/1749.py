# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re
from tqdm import tqdm

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1749_1.txt")
]
n, k = nums[0]
nums = nums[1:]
trebovania = nums[:n]
trebovania = [i[0] for i in trebovania]
models = nums[n:]
models.sort(key=lambda d: (d[1], -d[0]))
cur = 0
res = []
for tr in tqdm(sorted(trebovania)):
    for i in range(cur, len(models)):
        if models[i][0] >= tr:
            cur = i
            break
    res.append(models[cur])

print(sum([i[1] for i in res]), max([i[0] for i in res]))
