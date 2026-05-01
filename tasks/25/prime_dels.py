def find_prime_dels(num):
    res = set()
    i = 2
    while i <= int(num**0.5):
        while num % i == 0:
            res.add(i)
            num //= i
        i += 1
    return res
