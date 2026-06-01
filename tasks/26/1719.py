# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [
    [int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\1719_3.txt")
]

nums = nums[1:]
nums.sort(key=lambda d: (-sum(d[1:]), -d[1], -(d[2] + d[-1])))
res_id = nums[299][0]
inf_score = nums[299][1]
mx_id = 0
for i in nums[300:]:
    if i[1] == inf_score and i[0] > mx_id:
        mx_id = i[0]
print(res_id, mx_id)
