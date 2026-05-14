
# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip
from itertools import product,permutations


net = ip.ip_network('214.187.224.0/255.255.224.0',0)
res = 0
for i in net:
    a = bin(int(i))[2:].zfill(32)
    if a.count('1') % 6 and a.endswith('1000'):
        res+=1
print(res)