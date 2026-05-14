
# Solved by lfvbdghkjfgm
# https://lfvb.ru

from string import printable
print(printable)
alf=  printable

def dx(ch):
    return alf.index(ch)

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

for x in range(34):
    a = to_10([dx('g'),dx('p'),4,5,x,2],34)
    b = to_10([dx('p'),7,x],34)
    c = to_10([x,10,dx('i'),9,8],34)
    if (a+b*c)%13 == 0:
        print((a+b*c)//13)