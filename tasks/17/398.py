# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [int(i) for i in open("1")]

g = max([i for i in nums if str(i)[-1] == "7"])
res = []
for ind in range(len(nums) - 2):
    l = nums[ind : ind + 3]
    nc = [i for i in l if i % 2]
    b = [i for i in l if i > g]
    if len(nc) == 2 and len(b) == 1:
        res += l

print(len(res) / 3, sum(set(res)) / len(set(res)))

# Solved by Влад


a = [int(x) for x in open("test.txt")]
tr = []
ch = max([x for x in a if str(x)[-1] == "7"])
for i in range(len(a) - 2):
    if (
        (int((a[i] % 2) != 0) + int(a[i + 1] % 2 != 0) + int(a[i + 2] % 2 != 0)) == 2
    ) and ((int(a[i] > ch) + int(a[i + 1] > ch) + int(a[i + 2] > ch)) == 1):
        tr.append(a[i])
        tr.append(a[i + 1])
        tr.append(a[i + 2])
print(len(tr) / 3)
tr = set(tr)
print(sum(tr) / len(tr))
