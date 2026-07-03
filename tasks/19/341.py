# Solved by Владимир Д.


def g(s, p, end):
    if s >= 56:
        return p % 2 == end % 2
    if p == end:
        return 0

    moves = [g(s + 1, p + 1, end), g(s + 2, p + 1, end)]
    if s % 3 == 0:
        moves.append(g(s * 3, p + 1, end))

    if (p + 1) % 2 == end % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 56):
    p_moves = [s + 1, s + 2]
    if s % 3 == 0:
        p_moves.append(s * 3)

    if any(g(m, 1, 2) for m in p_moves):
        print(f"19: {s}")
        break

for s in range(1, 56):
    if not g(s, 0, 1) and g(s, 0, 3):
        print(f"20: {s}")


for s in range(1, 56):
    if g(s, 0, 6) and not g(s, 0, 4):
        print(f"21: {s}")
