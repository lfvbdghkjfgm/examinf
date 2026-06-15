# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip
from itertools import product, permutations

net = ip.ip_network("123.222.111.192/255.255.255.248", 0)
res = 0
for i in net:
    a = bin(int(i))[2:].zfill(32)
    if a[-8:].count("0") % 3:
        res += 1
print(res)

# Solved by София


import ipaddress

ct = 0
net = ipaddress.ip_network("123.222.111.192/255.255.255.248", 0)
for ip in net:
    a = bin(int(ip))[2:].zfill(32)
    if a[24:].count("0") % 3 != 0:
        ct += 1
print(ct)
