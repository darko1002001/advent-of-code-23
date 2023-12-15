def score_column(col):
    total = len(col)
    position = 0
    l = []
    for index, ch in enumerate(col):
        multiplier = total - position
        if ch == "O":
            l.append(multiplier)
            position += 1
        elif ch == "#":
            position = index + 1
    return sum(l)


def solve(section) -> int:
    # rocks = [
    #     (r, c) for r, row in enumerate(section) for c, ch in enumerate(row) if ch == "#"
    # ]
    return sum(score_column(col) for col in zip(*section))
