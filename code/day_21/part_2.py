import logging
from collections import deque

logger = logging.getLogger(__name__)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_plots(grid, sr, sc, steps):
    goal = set()
    seen = {(sr, sc)}
    q = deque([(sr, sc, steps)])
    while q:
        r, c, remaining_steps = q.popleft()
        if remaining_steps % 2 == 0:
            goal.add((r, c))
        if remaining_steps == 0:
            continue
        for dir_r, dir_c in directions:
            dr = r + dir_r
            dc = c + dir_c
            if (
                0 <= dr < len(grid)
                and 0 <= dc < len(grid[0])
                and (dr, dc) not in seen
                and grid[dr][dc] in ".S"
            ):
                seen.add((dr, dc))
                q.append((dr, dc, remaining_steps - 1))

    return len(goal)


def solve(grid, steps) -> int:
    sr, sc = next(
        (r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S"
    )

    size = len(grid)
    grid_width = steps // size - 1

    odd = (grid_width // 2 * 2 + 1) ** 2
    even = ((grid_width + 1) // 2 * 2) ** 2

    odd_points = find_plots(grid, sr, sc, size * 2 + 1)
    even_points = find_plots(grid, sr, sc, size * 2)

    corner_t = find_plots(grid, size - 1, sc, size - 1)
    corner_r = find_plots(grid, sr, 0, size - 1)
    corner_b = find_plots(grid, 0, sc, size - 1)
    corner_l = find_plots(grid, sr, size - 1, size - 1)

    small_tr = find_plots(grid, size - 1, 0, size // 2 - 1)
    small_tl = find_plots(grid, size - 1, size - 1, size // 2 - 1)
    small_br = find_plots(grid, 0, 0, size // 2 - 1)
    small_bl = find_plots(grid, 0, size - 1, size // 2 - 1)

    large_tr = find_plots(grid, size - 1, 0, size * 3 // 2 - 1)
    large_tl = find_plots(grid, size - 1, size - 1, size * 3 // 2 - 1)
    large_br = find_plots(grid, 0, 0, size * 3 // 2 - 1)
    large_bl = find_plots(grid, 0, size - 1, size * 3 // 2 - 1)

    return (
        odd * odd_points
        + even * even_points
        + corner_t
        + corner_r
        + corner_b
        + corner_l
        + (grid_width + 1) * (small_tr + small_tl + small_br + small_bl)
        + grid_width * (large_tr + large_tl + large_br + large_bl)
    )
