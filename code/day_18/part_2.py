import logging

from shapely import Polygon

logger = logging.getLogger(__name__)


def parse(line):
    # R 6 (#70c710)
    _, _, color = line.split()
    d = int(color[-2])
    color = color[2:-2]
    steps = int(color, 16)
    return d, steps


# 0 means R, 1 means D, 2 means L, and 3 means U.

directions = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


def dig(instructions):
    points = [(0, 0)]
    total_steps = 0
    for d, steps in instructions:
        rx, cx = directions[d]
        total_steps += steps
        r, c = points[-1]
        current = (r + rx * steps, c + cx * steps)
        points.append(current)
    return points, total_steps


def area(dig_site):
    # Shoelace Formula https://en.wikipedia.org/wiki/Shoelace_formula
    # Pick's theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
    points, perimeter_points_count = dig_site
    p = Polygon(points)
    i = int(p.area) - perimeter_points_count // 2 + 1
    return i + perimeter_points_count


def solve(lines) -> int:
    instructions = [parse(line) for line in lines]
    dig_site = dig(instructions)
    return area(dig_site)
