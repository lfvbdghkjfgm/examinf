# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("10.128.0.0/255.255.192.0", 0)
res = 0
for i in net:
    if bin(int(i))[2:].zfill(32).count("1") % 4 == 0:
        res += 1
print(res)
