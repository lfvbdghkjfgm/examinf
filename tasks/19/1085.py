# Solved by Владимир Д.


def g(s, p, end):
    if s < 32:
        return p in end

    if p >= max(end):
        return False

    moves = [g(s - 3, p + 1, end), g(s - 2, p + 1, end)]
    if s % 4 == 0:
        moves.append(g(s // 4, p + 1, end))

    return any(moves) if (p + 1) % 2 == (end[0] % 2) else all(moves)


print([s for s in range(32, 200) if g(s, 0, [2])])
print([s for s in range(32, 200) if g(s, 0, [3])])
print([s for s in range(32, 200) if g(s, 0, [2, 4]) and not g(s, 0, [2])])

# Solved by Аня


def g(s, p):
    if s < 32 and (p == 2 or p == 4):
        return 1
    if s >= 32 and p == 4:
        return 0
    if s < 32 and p != 4:
        return 0
    if p % 2 == 0:
        if s % 4 == 0:
            return g(s - 3, p + 1) and g(s - 2, p + 1) and g(s // 4, p + 1)
        else:
            return g(s - 3, p + 1) and g(s - 2, p + 1)
    else:
        if s % 4 == 0:
            return g(s - 3, p + 1) or g(s - 2, p + 1) or g(s // 4, p + 1)
        else:
            return g(s - 3, p + 1) or g(s - 2, p + 1)


for S in range(32, 1000):
    if g(S, 0):
        print(S)
