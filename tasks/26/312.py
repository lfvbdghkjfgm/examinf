nums = [int(x) for x in open('1.txt')]
nums = nums[1:]
nums.sort()

used_nums = []
res = 0
for i in range(len(nums)):
    if i in used_nums:
        continue
    a = nums[i]
    for j in range(i+1,len(nums)):
        if j in used_nums:
            continue
        b = nums[j]
        if a+b == 100:
            res+=1
            used_nums.append(i)
            used_nums.append(j)
            break
        elif a+b > 100:
            break
print(res)