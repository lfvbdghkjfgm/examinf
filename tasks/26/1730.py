# Solved by lfvbdghkjfgm
# https://lfvb.ru

nums = [int(x) for x in open(r"C:\Users\aatop\Downloads\1730_3.txt")]
ct = 9
nums = nums[1:]
nums.sort()
dor_tor_ct = len(nums) // ct
dor_tov = nums[-dor_tor_ct:]
desh_tov = nums[:-dor_tor_ct]
first_sum = sum(desh_tov)
nums.sort(reverse=True)
second_sum = 0
for i, x in enumerate(nums, 1):
    if i % ct != 0:
        second_sum += x

print(first_sum, second_sum)
