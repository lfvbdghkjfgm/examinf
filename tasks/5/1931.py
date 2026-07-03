# Solved by Аня


s = []
for n in range(11, 1000):
    r = bin(n)[2:]
    if r.count("11") == 1:
        r = "10" + r[2:] + "0"
    else:
        r = "11" + r[2:] + "1"
    r = int(r, 2)
    if r <= 1500:
        s.append([n, r])
print(max(s, key=lambda x: x[1]))

# Solved by Анастасия


d = []
for n in range(11, 1000):
    r = bin(n)[2:]
    if r.count("11") == 1:
        r = "10" + r[2:] + "0"
    else:
        r = "11" + r[2:] + "1"
    r = int(r, 2)
    if r == 1492:
        print(n, r)
#         d.append(r)
# print(max(d))
