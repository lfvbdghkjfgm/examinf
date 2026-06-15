# Solved by Анастасия


import ipaddress

for x in ipaddress.ip_network("115.15.60.15/255.255.128.0", 0):
    print(x)
# 11515127255
