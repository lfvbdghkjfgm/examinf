# Solved by Анастасия


import ipaddress

for x in ipaddress.ip_network("146.180.173.153/255.192.0.0", 0):
    if (bin(int(x))[2:].zfill(32)).count("1") >= 4:
        print(x)

146191255254

# Solved by Аня


import ipaddress

for x in ipaddress.ip_network("146.180.173.153/255.192.0.0", 0):
    if bin(int(x))[2:].zfill(32).count("1") >= 4:
        print(x)
