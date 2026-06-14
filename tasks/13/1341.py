# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("98.112.180.225/255.255.240.0", 0)
print("".join(str(list(net.hosts())[-1]).split(".")))
