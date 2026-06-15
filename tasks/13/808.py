# Solved by Владимир Д.

import ipaddress

ip = "121.96.174.205"

for mask_len in range(32, -1, -1):
    net = ipaddress.ip_network(f"{ip}/{mask_len}", strict=False)

    count_12_ones = 0
    for ip in net:
        if bin(int(ip)).count("1") == 12:
            count_12_ones += 1

    if count_12_ones == 10:
        print(mask_len)
        break
