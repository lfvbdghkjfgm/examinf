# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip

net = ip.ip_network("95.24.16.0/255.255.240.0", 0)
mx = [0, ""]
for i in net.hosts():
    if bin(int(i)).count("1") >= mx[0]:
        mx = [bin(int(i)).count("1"), i]
t = list(map(int, str(mx[1]).split(".")))
print(t[-2] + t[-1])
