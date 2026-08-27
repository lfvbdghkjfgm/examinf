# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("167.89.100.150/255.255.248.0", 0)
print("".join(str(list(net.hosts())[0]).split(".")))
