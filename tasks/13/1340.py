# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("135.13.142.29/255.255.255.128", 0)
print("".join(str(list(net.hosts())[-1]).split(".")))
