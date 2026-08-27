# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("172.16.80.0/255.255.248.0", 0)
res = 0
for i in net:
    if bin(int(i))[2:].zfill(32).count("1") % 2 != 0:
        res += 1
print(res)
