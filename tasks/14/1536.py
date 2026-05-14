
# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product,permutations

def to_10(l,ss):
    res= 0
    for s,num in enumerate(l[::-1]):
        res+=num*ss**s
    return res

def to_ss(num,ss):
    res= []
    while num > 0:
        res.append(num%ss)
        num//=ss
    return res[::-1]


for p in range(10,200):
    for x,y,z,w in permutations(range(p),r=4):
        a = to_10([y,0,7,x],p)
        b = to_10([w,y,9,z],p)
        c = to_10([z,x,y,x,y],p)
        if a+b == c:
            print(to_10([x,y,z,w],p))
            exit()