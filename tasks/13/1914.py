# Solved by Аня


import ipaddress

for x in ipaddress.ip_network("172.45.129.10/255.240.0.0", 0):
    print(x)

# Solved by Владимир Д.


import ipaddress

for ip in ipaddress.ip_network("172.45.129.10/255.240.0.0", strict=False):
    print(ip)
