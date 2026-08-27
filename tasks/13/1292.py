# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("143.168.72.213/255.255.255.240", 0)
print("".join(str(list(net.hosts())[-1]).split(".")))
