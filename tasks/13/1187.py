# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("158.214.121.40/255.255.255.224", 0)
print(list(net.hosts())[0])

# Solved by Анастасия

import ipaddress

ct = 0
for x in ipaddress.ip_network("158.214.121.40/255.255.255.224", 0):
    x = bin(int(x))[2:].zfill(32)
    ct += 1
print(x)
