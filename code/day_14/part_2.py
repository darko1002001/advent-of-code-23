import logging

logger = logging.getLogger(__name__)


def score_column(col):
    total = len(col)
    position = 0
    new_col = [*"." * total]
    for index, ch in enumerate(col):
        if ch == "O":
            new_col[position] = "O"
            position += 1
        elif ch == "#":
            position = index + 1
            new_col[index] = "#"
    return "".join(new_col)


def run(section):
    return tuple(score_column(col) for col in section)


def rotate(section):
    return tuple(row[::-1] for row in section)


def solve(section) -> int:
    section = tuple(section)
    seen = {section}
    list_ = [seen]
    i = 0
    while True:
        i += 1
        for _ in range(4):
            section = run(zip(*section))
            section = rotate(section)
        if section in seen:
            break
        list_.append(section)
        seen.add(section)
    cycle = list_.index(section)
    section = list_[(1000000000 - cycle) % (i - cycle) + cycle]
    return sum(row.count("O") * (len(section) - r) for r, row in enumerate(section))
