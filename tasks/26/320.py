k = 400

nums = [int(i) for i in open('1.txt')]
nums = sorted(nums)[::-1]
res = []
res1 = []
right_indexes = list(range(len(nums)))
for i in range(len(nums)):
    a = nums[i]
    if i not in right_indexes:
        continue
    for j in right_indexes[::-1]:
        b = nums[j]
        if i == j:
            continue
        if j not in right_indexes:
            continue
        if b + a <= k:
            right_indexes.remove(i)
            right_indexes.remove(j)
            res.append([a,b])
            break
    else:
        res1.append(a)

print(len(res),sum(res1))