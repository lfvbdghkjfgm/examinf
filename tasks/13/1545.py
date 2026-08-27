# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("95.24.30.144/255.255.248.0", 0)
t = list(map(int, str(list(net.hosts())[0]).split(".")))
print(sum(t))
