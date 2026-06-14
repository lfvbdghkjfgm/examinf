# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("111.222.0.124/255.255.224.0", 0)

for i in net:
    s = bin(int(i))[2:].zfill(32)
    if (s.count("0") * s.count("1")) % 2 == 1:
        t = list(map(int, str(i).split(".")))
        print(sum(t))
