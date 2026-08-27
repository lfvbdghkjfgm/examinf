# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

nums = [[int(i) for i in x.split()] for x in open("1.txt")]
k = nums[0][1]
nums = sorted(nums[1:])
operators = [-1] * k
last_operator = 0
res = 0
for a, b in nums:
    t = [i for i in range(len(operators)) if operators[i] <= a]
    if t:
        i = t[0]
    else:
        i = operators.index(min(operators))
    if operators[i] < b:
        last_operator = i + 1
        operators[i] = b
        res += 1
print(res, last_operator)
