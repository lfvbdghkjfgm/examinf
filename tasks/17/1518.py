

nums = [int(i) for i in open('1.txt')]
glob = min([i for i in nums if i>0 and i%1000 == 102])
res = []
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            a,b,c = nums[i],nums[j],nums[k]
            d = [i for i in [a,b,c] if len(str(i))== 5 and i>0 and i%3 ==0]
            if len(d) == 2 and (a**2+b**2+c**2) % glob == 0:
                res.append((a+b+c)/3)
print(len(res),min(res))
