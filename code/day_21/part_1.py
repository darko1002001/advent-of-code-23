import logging
from collections import deque

logger = logging.getLogger(__name__)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_plots(grid, start, steps):
    sr, sc = start
    seen = {start}
    q = deque([(sr, sc, steps)])
    goal = set()
    while q:
        r, c, remaining_steps = q.popleft()
        if remaining_steps == 0:
            goal.add((r, c))
            continue
        for dir_r, dir_c in directions:
            dr = r + dir_r
            dc = c + dir_c
            next_item = (dr, dc, remaining_steps - 1)
            if (
                0 <= dr < len(grid)
                and 0 <= dc < len(grid[0])
                and next_item not in seen
                and grid[dr][dc] in ".S"
            ):
                seen.add(next_item)
                q.append(next_item)

    return len(goal)


def solve(grid, steps) -> int:
    start = next(
        (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S"
    )
    logger.info(start)
    return find_plots(grid, start, steps)
