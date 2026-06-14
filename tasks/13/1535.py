# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

for mask in range(32, 0, -1):
    net = ip.ip_network(f"132.118.34.161/{mask}", 0)
    res = 0
    for i in net:
        if bin(int(i)).count("1") == 13:
            res += 1
    if res == 35:
        print(32 - mask)
        break
