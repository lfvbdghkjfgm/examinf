# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

net = ip.ip_network("210.189.23.15/255.255.248.0", 0)
print("".join(str(net.network_address).split(".")))
