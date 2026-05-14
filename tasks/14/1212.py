
# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

def from_ss(l,ss):
    res = 0
    for a,i in enumerate(l[::-1]):
        res+=i*ss**a
    return res

def to_ss(num,ss):
    res = []
    while num >=ss:
        res.append(num%ss)

        num//=ss
    res.append(num)
    return res[::-1]

for x in range(37):
    a = from_ss([9,8,x,3,1],37)
    b = from_ss([1,x,9,2,4],37)
    if (a+b)%21 == 0:
        print((a+b)/21)