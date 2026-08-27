# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import ipaddress as ip

addr1 = ip.ip_address("126.115.78.15")
addr2 = ip.ip_address("126.115.84.26")

for mask in range(32, 0, -1):
    net = ip.ip_network(f"126.115.78.15/{mask}", 0)
    if addr1 in net.hosts() and addr2 in net.hosts():
        res = 0
        for i in net:
            if bin(int(i)).count("1") == 22:
                res += 1
        print(res)
        break
