# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("83.152.68.115/255.255.224.0", 0)
print("".join(str(list(net.hosts())[-1]).split(".")))
