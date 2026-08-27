# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import gcd

a = 640 * 370 // gcd(640, 370)
print(a * 680 // gcd(a, 680))
