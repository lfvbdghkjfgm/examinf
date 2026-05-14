# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [int(x) for x in open("1.txt")]
nums = nums[1:]
nums.sort()

sr = int(sum(nums) / len(nums))
m = nums[len(nums) // 2]

res = 0

for i in nums:
    if min(sr, m) <= i <= max(sr, m):
        res += 1
    if i > max(m, sr):
        break
print(res)