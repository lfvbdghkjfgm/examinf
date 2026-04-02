stat = [0]*101
nums = [int(x) for x in open('1.txt')]
nums = nums[1:]
for i in nums:
    stat[i] +=1
res = 0
for i in range(50):
    res += min(stat[i],stat[100-i])
res += stat[50] // 2
print(res)