# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


k = 1
for i in range(2422000, 2422080):
    if is_prime(i):
        print(k, i)
        k += 1
