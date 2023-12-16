import logging

logger = logging.getLogger(__name__)

# fmt: off
options = {
    ("R", "."): ["R"],
    ("R", "-"): ["R"],
    ("R", "|"): ["T", "B"],
    ("R", "\\"): ["B"],
    ("R", "/"): ["T"],

    ("T", "."): ["T"],
    ("T", "-"): ["R", "L"],
    ("T", "|"): ["T"],
    ("T", "\\"): ["L"],
    ("T", "/"): ["R"],

    ("B", "."): ["B"],
    ("B", "-"): ["R", "L"],
    ("B", "|"): ["B"],
    ("B", "\\"): ["R"],
    ("B", "/"): ["L"],

    ("L", "."): ["L"],
    ("L", "-"): ["L"],
    ("L", "|"): ["T", "B"],
    ("L", "\\"): ["T"],
    ("L", "/"): ["B"],
}
# fmt: on


directions = {"R": (0, 1), "L": (0, -1), "T": (-1, 0), "B": (1, 0)}


def solve_for_start(inputs, start):
    seen = set()
    total = set()
    q = [start]
    while q:
        item = q.pop()
        r, c, d = item
        dx, dy = directions[d]
        r += dx
        c += dy
        if 0 <= r < len(inputs) and 0 <= c < len(inputs[0]) and (r, c, d) not in seen:
            seen.add((r, c, d))
            ch = inputs[r][c]
            next_ = options[(d, ch)]
            next_pairs = [(r, c, n) for n in next_]
            q.extend(next_pairs)
            total.add((r, c))
    return len(total)


def solve(inputs) -> int:
    pairs = []
    for r in range(0, len(inputs)):
        pairs.append((r, -1, "R"))
        pairs.append((r, len(inputs[0]), "L"))
    for c in range(0, len(inputs[0])):
        pairs.append((-1, c, "B"))
        pairs.append((len(inputs), c, "T"))

    return max([solve_for_start(inputs, p) for p in pairs])
