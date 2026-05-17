# Solved by lfvbdghkfjgm
# https://lfvb.ru


def is_prime(num):
    if num in [0, 1]:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def to_243(num):
    res = []
    while num:
        res.append(num % 243)
        num //= 243

    return res[::-1]


t = to_243(20 * 3**243 + 17 * 81**70 + 14 * 243**35 + 254 - 224 * 3**30)
print(len([i for i in t if i < 20 and is_prime(i)]))
