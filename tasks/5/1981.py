# Solved by Анастасия


def v3(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


d = []
for n in range(4, 1000):
    r = v3(n)
    if (r.count("0") + r.count("2")) > r.count("1"):
        r += r[-2:]
    else:
        r = r.replace("0", "1")
        r = r.replace("1", "2")
        r = r.replace("2", "0")
    r = int(r, 3)
    if r < 315:
        d.append(r)
print(max(d))

# Solved by Аня


s = []


def v3(n):
    s = ""
    while n > 0:
        s += str(n % 3)
        n //= 3
    return s[::-1]


for N in range(4, 1000):
    r = v3(N)
    if r.count("2") + r.count("0") > r.count("1"):
        r = r + r[-2:]
    else:
        r = r.replace("0", "1")
        r = r.replace("1", "2")
        r = r.replace("2", "0")
    r = int(r, 3)
    if r < 315:
        s.append(r)
print(max(s))
