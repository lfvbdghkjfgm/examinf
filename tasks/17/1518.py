# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [int(i) for i in open("1.txt")]
glob = min([i for i in nums if i > 0 and i % 1000 == 102])
res = []
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            a, b, c = nums[i], nums[j], nums[k]
            d = [i for i in [a, b, c] if len(str(i)) == 5 and i > 0 and i % 3 == 0]
            if len(d) == 2 and (a**2 + b**2 + c**2) % glob == 0:
                res.append((a + b + c) / 3)
print(len(res), min(res))

# Solved by Владимир Д.


l = [int(d) for d in open("examinf/17/1518.txt")]
mn_102 = min([d for d in l if d > 0 and d % 1000 == 102])
ct = 0
mn_trio = float("inf")

for i in range(len(l) - 2):
    for j in range(i + 1, len(l) - 1):
        for k in range(j + 1, len(l)):
            a, b, c = l[i], l[j], l[k]
            usl1 = [
                d for d in (a, b, c) if len(str(abs(d))) == 5 and d % 3 == 0 and d > 0
            ]
            if len(usl1) == 2:
                if (a**2 + b**2 + c**2) % mn_102 == 0:
                    ct += 1
                    mn_trio = min(mn_trio, (a + b + c) // 3)

print(ct, mn_trio)
print(mn_102)
