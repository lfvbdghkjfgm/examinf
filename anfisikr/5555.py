for n in range(1, 10000):
    a = bin(n)[2:]
    if n % 5 == 0:
        a = a + '11'
    else:
        a = a + bin(n // 5)[2:]
    r = int(a, 2)
    if r >= 783:
        print(n)
        break