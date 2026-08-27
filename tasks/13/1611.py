# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("46.29.170.214/255.255.128.0", 0)

for i in net.hosts():
    t = list(map(int, str(i).split(".")))
    if max(t) == sum(sorted(t)[:3]):
        print(*t, sep="")
