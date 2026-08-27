# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

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


# Solved by Григорий Б.


import math

l = [int(d) for d in open("998.txt")]
A = []
for x in range(len(l) - 1):
    if math.gcd(l[x], l[x + 1]) == 1:
        if l[x] % 2 != l[x + 1] % 2:
            A.append(l[x] + l[x + 1])
print(len(A), min(A))

# Solved by Глеб Г.


q = []


def f(n):
    l = []
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            l.append(x)
            l.append(n // x)
    return sorted(set(l))


l = [int(d) for d in open("35.txt")]
for x in range(len(l) - 1):
    k = 0
    a = f(l[x])
    b = f(l[x + 1])
    for y in a:
        if y not in b:
            k += 1
            if k == len(a):
                if (l[x] % 2 == 0 and l[x + 1] % 2 != 0) or (
                    l[x] % 2 != 0 and l[x + 1] % 2 == 0
                ):
                    q.append(l[x] + l[x + 1])
print(len(q), min(q))
