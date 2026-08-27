# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re


def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for i in range(22768, 10**8, 22768):
    if re.fullmatch(r"1(?:[1-9][0-9]*)03\d*6\d*", str(i)):
        m = re.findall(r"1([1-9][0-9]*)03\d*6\d*", str(i))
        if not is_prime(int(m[0])):
            print(i, m[0])
