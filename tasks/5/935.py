# Solved by Анастасия


d = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if (sum(map(int, r))) % 4 == 0:
        r += "1111"
    elif (sum(map(int, r))) % 3 == 0:
        r += "111"
    else:
        r += "11"
    r = int(r, 2)
    if r < 450:
        d.append(r)
print(max(d))
