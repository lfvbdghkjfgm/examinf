# Solved by Виктор Г.


k = 0
for n in range(10000, 100000):
    r = oct(n)[2:]
    r = r.replace("1", "2")
    r = r.replace("3", "2")
    r = r.replace("5", "2")
    r = r.replace("7", "2")
    r += str(n % 8)
    r = int(r, 8)
    r = oct(r)[2:]
    r = r.replace("1", "2")
    r = r.replace("3", "2")
    r = r.replace("5", "2")
    r = r.replace("7", "2")
    r += str(n % 8)
    q = int(r, 8)
    if q % 2023 == 0:
        k += n
print(k)

# Solved by Илья М.


k = 0
for N in range(10000, 99999):
    r = oct(N)[2:]
    r = r.replace("1", "2")
    r = r.replace("3", "2")
    r = r.replace("5", "2")
    r = r.replace("7", "2")
    r = r + str(N % 8)
    r = int(r, 8)
    r = oct(r)[2:]
    r = r.replace("1", "2")
    r = r.replace("3", "2")
    r = r.replace("5", "2")
    r = r.replace("7", "2")
    r = r + str(N % 8)
    R = int(r, 8)
    if R % 2023 == 0:
        k += N
print(k)
