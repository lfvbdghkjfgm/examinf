# Solved by Аня


def v38(n):
    s = []
    while n > 0:
        s.append(n % 38)
        n //= 38
    return s[::-1]


sp = []
for x in range(0, 20_001):
    d = 10024**2 + 17 * 10024 + 53
    print(d)
    d = v38(d)
#     for y in d:
#         if d.count(10) == 3:
#         # sp.append(d.count(10))
# # print(max(sp))
#             print(x)

# Solved by Анастасия


def v38(n):
    s = []
    while n > 0:
        s.append(n % 38)
        n //= 38
    return s[::-1]


sp = []
# for x in range(0, 20_001):
#     d = x ** 2 + 17*x + 53
#     # print(d)
#     d = v38(d)
#     if d.count(10) == 3:
#         print(x)
for x in range(0, 20_001):
    d = 10024**2 + 17 * 10024 + 53
    print(d)
