from collections import defaultdict
from itertools import combinations


def find_empty(inputs):
    filled_rows = defaultdict(lambda: False)
    filled_cols = defaultdict(lambda: False)
    galaxies = []
    for r, row in enumerate(inputs):
        for c, char in enumerate(row):
            if char == "#":
                filled_rows[r] = True
                filled_cols[c] = True
                galaxies.append((r, c))
    return filled_rows, filled_cols, galaxies


def create_range(i: int, j: int):
    if i < j:
        return range(i, j)
    else:
        return range(i, j, -1)


def extra_space(i, j, filled) -> int:
    return sum([0 if filled[index] else (1000000 - 1) for index in create_range(i, j)])


def distance(pair, filled_rows, filled_cols):
    first, second = pair
    row1, col1 = first
    row2, col2 = second
    total = (
        abs(row1 - row2)
        + abs(col1 - col2)
        + extra_space(row1, row2, filled_rows)
        + extra_space(col1, col2, filled_cols)
    )
    return total


def solve(inputs) -> int:
    filled_rows, filled_cols, galaxies = find_empty(inputs)
    pairs = list(combinations(galaxies, 2))
    return sum([distance(pair, filled_rows, filled_cols) for pair in pairs])
