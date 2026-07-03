# Solved by Владимир Д.


def g(s, p, end):
    if s >= 58:
        return p % 2 == end % 2

    if p == end:
        return 0

    moves = [g(s + 1, p + 1, end), g(s + 4, p + 1, end), g(s * 2, p + 1, end)]

    if (p + 1) % 2 == end % 2:
        return any(moves)

    else:
        return all(moves)


for s in range(1, 58):
    if g(s, 0, 2):
        print(s)
        break

print("----")
for s in range(1, 58):
    if not g(s, 0, 1) and g(s, 0, 3):
        print(s)

print("----")
for s in range(1, 58):
    if not g(s, 0, 2) and g(s, 0, 4):
        print(s)
        break

# Solved by Аня


def g(s, p):
    if s >= 58 and (p == 4 or p == 2):
        return 1
    if s < 58 and p == 4:
        return 0
    if s >= 58 and p < 4:
        return 0

    if p % 2 == 0:
        return g(s + 1, p + 1) and g(s + 4, p + 1) and g(s * 2, p + 1)
    else:
        return g(s + 1, p + 1) or g(s + 4, p + 1) or g(s * 2, p + 1)


for S in range(1, 57):
    if g(S, 0):
        print(S)
