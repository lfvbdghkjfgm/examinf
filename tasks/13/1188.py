# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("5.2.5.0/255.255.0.0", 0)
res = 0
for i in net:
    if bin(int(i))[2:].zfill(32).count("0") % 25 == 0:
        res += 1
print(res)
