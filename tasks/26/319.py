nums = [int(x) for x in open('1.txt').readlines()[1:]]
k = 9
nums.sort()
nums = nums[::-1]

res = []

while nums:
    block = [nums[0]]
    for i in nums:
        if block[-1] - i >= k:
            block.append(i)
    res.append(block)
    for i in block:
        nums.remove(i)
print(len(res),len(max(res,key=len)))