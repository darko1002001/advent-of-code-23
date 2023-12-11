from collections import defaultdict
from itertools import combinations


def find_empty(inputs):
    filled_rows = defaultdict(lambda: False)
    filled_cols = defaultdict(lambda: False)
    galaxies = []
    index = 1
    for r, row in enumerate(inputs):
        for c, char in enumerate(row):
            if char == "#":
                filled_rows[r] = True
                filled_cols[c] = True
                galaxies.append((r, c, index))
                index += 1
    return filled_rows, filled_cols, galaxies


def extra_space(i, j, filled) -> int:
    return sum([0 if filled[index] else 1 for index in range(min(i, j), max(i, j))])


def distance(pair, filled_rows, filled_cols):
    first, second = pair
    row1, col1, num1 = first
    row2, col2, num2 = second
    distance = abs(row1 - row2) + abs(col1 - col2)
    total = (
        distance
        + extra_space(row1, row2, filled_rows)
        + extra_space(col1, col2, filled_cols)
    )
    # print(f"{num1}-{num2} | {distance=} {pair=}, {total=}")
    return total


def solve(inputs) -> int:
    filled_rows, filled_cols, galaxies = find_empty(inputs)
    pairs = list(combinations(galaxies, 2))
    # print(len(pairs))
    return sum([distance(pair, filled_rows, filled_cols) for pair in pairs])
