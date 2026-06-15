# Solved by Анастасия


# import math
# def g(s,p):
#     if s<=20262026 and p==2:
#         return 1
#     if s>20262026 and p==2:
#         return 0
#     if s<=20262026 and p<2:
#         return 0
#     if p%2==0:
#         return g(s-2,p+1) and g(s-6,p+1) and g(math.ceil(s/7),p+1)
#     else:
#         return g(s - 2, p + 1) or g(s - 6, p + 1) or g(math.ceil(s / 7), p + 1)
# for S in range(20262027,10**10):
#     if g(S,0):
#         print(S)


# import math
# def g(s,p):
#     if s<=20262026 and p==3:
#         return 1
#     if s>20262026 and p==3:
#         return 0
#     if s<=20262026 and p<3:
#         return 0
#     if p%2!=0:
#         return g(s-2,p+1) and g(s-6,p+1) and g(math.ceil(s/7),p+1)
#     else:
#         return g(s - 2, p + 1) or g(s - 6, p + 1) or g(math.ceil(s / 7), p + 1)
# for S in range(20262027,10**10):
#     if g(S,0):
#         print(S)


import math


def g(s, p):
    if s <= 20262026 and (p == 2 or p == 4):
        return 1
    if s > 20262026 and p == 4:
        return 0
    if s <= 20262026 and p < 4:
        return 0
    if p % 2 == 0:
        return g(s - 2, p + 1) and g(s - 6, p + 1) and g(math.ceil(s / 7), p + 1)
    else:
        return g(s - 2, p + 1) or g(s - 6, p + 1) or g(math.ceil(s / 7), p + 1)


for S in range(20262027, 10**10):
    if g(S, 0):
        print(S)
