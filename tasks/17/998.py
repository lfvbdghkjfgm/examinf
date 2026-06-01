# Solved by lfvbdghkfjgm
# https://lfvb.ru

from math import gcd

nums = [int(i) for i in open(r"C:\Users\aatop\Downloads\998_1.txt")]

res = []

for i in range(len(nums) - 1):
    a = nums[i]
    b = nums[i + 1]
    if gcd(a, b) == 1 and a % 2 != b % 2:
        res.append(a + b)
print(len(res), min(res))


# Другой способ искать НОД двух чисел
def another_gcd(a, b):
    while b:
        a, b = b, a % b
    return a
