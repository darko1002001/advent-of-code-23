import logging
from heapq import heappush, heappop

logger = logging.getLogger(__name__)


directions = {
    "R": (0, 1),
    "D": (1, 0),
    "U": (-1, 0),
    "L": (0, -1),
}

options = {
    "R": ["U", "D"],
    "L": ["U", "D"],
    "D": ["L", "R"],
    "U": ["L", "R"],
}


def next_moves(current, grid):
    cost, r, c, d, current_steps = current
    next_ = []
    if current_steps < 3:
        dr, dc = directions[d]
        next_.append((dr, dc, d, current_steps + 1))
    for o in options[d]:
        dr, dc = directions[o]
        next_.append((dr, dc, o, 1))

    return [
        (cost + int(grid[r + dr][c + dc]), r + dr, c + dc, d, steps)
        for dr, dc, d, steps in next_
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0])
    ]


def solve(grid) -> int:
    destination = (len(grid) - 1, len(grid[0]) - 1)
    q = [(0, 0, 0, "D", 0), (0, 0, 0, "R", 0)]
    seen = set()

    while q:
        item = heappop(q)
        cost, r, c, d, steps = item
        if (r, c) == destination:
            return cost
        if (r, c, d, steps) in seen:
            continue
        seen.add((r, c, d, steps))
        next_ = next_moves(item, grid)
        for n in next_:
            heappush(q, n)
