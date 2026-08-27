# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

# РРµС€РµРЅРёРµ 1
nums = [int(x) for x in open("1.txt")]
nums = nums[1:]
nums.sort()

used_nums = []
res = 0
for i in range(len(nums)):
    if i in used_nums:
        continue
    a = nums[i]
    for j in range(i + 1, len(nums)):
        if j in used_nums:
            continue
        b = nums[j]
        if a + b == 100:
            res += 1
            used_nums.append(i)
            used_nums.append(j)
            break
        elif a + b > 100:
            break
print(res)

# РРµС€РµРЅРёРµ 2

stat = [0] * 101
nums = [int(x) for x in open("1.txt")]
nums = nums[1:]
for i in nums:
    stat[i] += 1
res = 0
for i in range(50):
    res += min(stat[i], stat[100 - i])
res += stat[50] // 2
print(res)
