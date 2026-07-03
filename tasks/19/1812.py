# Solved by Владимир Д.


def g(s, p, end):
    if s >= 231:
        return p in end

    if p >= max(end):
        return False

    if p % 2 == 0:
        moves = [g(s + 3, p + 1, end), g(s * 3, p + 1, end)]
    else:
        moves = [g(s + 5, p + 1, end), g(s * 3, p + 1, end)]

    if ((p + 1) % 2) == (end[0] % 2):
        return any(moves)

    else:
        return all(moves)


print([s for s in range(10, 121) if g(s, 0, [2])])
print([s for s in range(10, 121) if g(s, 0, [3])])
print([s for s in range(10, 121) if g(s, 0, [2, 4]) and not g(s, 0, [2])])
