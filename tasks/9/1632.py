# Solved by lfvbdghkjfgm
# https://lfvb.ru

res = 0

nums = [[int(i) for i in x.split()] for x in open("1")]

for a, x in enumerate(nums, 1):
    p = [i for i in x if x.count(i) > 1]
    np = [i for i in x if x.count(i) == 1]
    if sum(x) % 2 == 1 and sum(p) ** 2 > sum(np) ** 2 and p and np:
        res = a
print(res)

# Solved by Владимир Д.

l = [[int(d) for d in x.split()] for x in open("other/examinf/9/1632.txt")]
ct = 0

for x in l:
    ct += 1
    povt = [d for d in x if x.count(d) > 1]
    nepovt = [d for d in x if x.count(d) == 1]
    if povt and nepovt:
        if sum(povt) ** 2 > sum(nepovt) ** 2:
            if sum(x) % 2 != 0:
                print(ct)
