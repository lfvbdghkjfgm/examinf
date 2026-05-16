# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip


net = ip.ip_network('158.214.121.40/255.255.255.224',0)
print(list(net.hosts())[0])