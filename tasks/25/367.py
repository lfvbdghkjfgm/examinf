# Solved by Владимир Д.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)
    return sorted(set(dls))


count = 0
num = 8120141

while count < 5:
    all_dels = dels(num)
    for p1 in all_dels:
        if is_prime(p1):
            p2 = num // p1
            if is_prime(p2):
                if str(p1).count("2") == 2 and str(p2).count("2") == 2:
                    print(num, max(p1, p2))
                    count += 1
                    break
    num += 1
