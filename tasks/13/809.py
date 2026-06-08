# Solved by София

import ipaddress

ct = 0
for mask in range(15, 33):
    ct = 0
    net = ipaddress.ip_network(f"143.131.211.37/{mask}", 0)
    for ip in net:
        a = bin(int(ip))[2:].zfill(32)
        if a.count("1") == 10:
            ct += 1
    if ct == 15:
        print(mask)
