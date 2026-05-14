
# Solved by lfvbdghkjfgm
# https://lfvb.ru

def to_ss(num,ss):
    res = []
    while num >0 :
        res.append(num%ss)
        num//=ss
    return res[::-1]

a = 5**17+5**12
r = [0,0]
for x in range(1,4001):
    d = to_ss(a-x,5)
    if d.count(0) > r[0]:
        r = [d.count(0),x]

print(r)