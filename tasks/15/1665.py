# Solved by Мария


for A in range(1, 100000):
    can = True
    for x in range(1, 100000):
        if ((x % 465 == 0) <= ((x % A != 0) <= (x % 385 != 0))) == 0:
            can = False
            break
    if can == True:
        print(A)
