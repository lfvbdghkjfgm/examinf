# Solved by Владимир Д.


def g(s, p, end):
    if s >= 471:
        return p in end

    if p >= max(end):
        return False

    moves = [g(s + 4, p + 1, end), g(s + 7, p + 1, end), g(s * 4, p + 1, end)]

    if ((p + 1) % 2) == (end[0] % 2):
        return any(moves)

    else:
        return all(moves)


print([s for s in range(1, 471) if g(s, 0, [2])])
print([s for s in range(1, 471) if g(s, 0, [3])])
print(sum([s for s in range(1, 471) if g(s, 0, [2, 4]) and not g(s, 0, [2])]))
