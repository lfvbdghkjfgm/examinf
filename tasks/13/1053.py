# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("69.121.128.142/255.255.252.0", 0)

print(list(net.hosts())[-1])