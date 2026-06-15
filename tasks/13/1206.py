# Solved by Аня


import ipaddress

s = []
for mask in range(15, 33):
    n1 = ipaddress.ip_network(f"200.154.190.12/{mask}", 0)
    n2 = ipaddress.ip_network(f"200.154.184.0/{mask}", 0)
    if n1 == n2:
        s.append(mask)
print(max(s))

# Solved by Анастасия


import ipaddress

s = []
for mask in range(15, 33):
    n1 = ipaddress.ip_network(f"200.154.190.12/{mask}", 0)
    n2 = ipaddress.ip_network(f"200.154.184.0/{mask}", 0)
    if n1 == n2:
        s.append(mask)
print(max(s))

# Solved by Владимир Д.


import ipaddress

s = []
for mask in range(15, 33):
    n1 = ipaddress.ip_network(f"200.154.190.12/{mask}", strict=False)
    n2 = ipaddress.ip_network(f"200.154.184.0/{mask}", strict=False)
    if n1 == n2:
        s.append(mask)

print(max(s))
