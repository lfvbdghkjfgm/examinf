# Solved by Владимир Д.


def g(s, p, end):
    if s <= 1:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s - 1, p + 1, end)]
    if s >= 4:
        moves.append(g(s - 4, p + 1, end))
    if s % 3 == 0:
        moves.append(g(s // 3, p + 1, end))

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


print([s for s in range(4, 101) if g(s, 0, 2)])
print([s for s in range(4, 101) if not g(s, 0, 1) and g(s, 0, 3)])
print([s for s in range(4, 101) if not g(s, 0, 2) and g(s, 0, 4)])
